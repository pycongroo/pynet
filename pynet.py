"""Modulo con funciones para descarga de archivos."""
import os
import sys
import requests

from modules.colors import m_aviso
from modules.colors import m_error
from modules.colors import m_accion
from modules.colors import m_interr
from modules.colors import m_info
from modules.colors import fg_VERDE
from modules.colors import END_char
from modules.colors import PROPS
import modules.extras

class NetHandler():

    def __init__(self, sesion=requests.session()):
        self.sesion = sesion

    def request_get(self, url, **kargs):
        """Request modificado para muestreo en colores."""
        m_accion('requesting to %s' % url)
        try:
            req_obj = self.sesion.get(url, **kargs)
            m_aviso('%s %s' % (req_obj.status_code, req_obj.reason))
            return req_obj
        except KeyboardInterrupt:
            m_interr('Cancelado por usuario')
            raise KeyboardInterrupt
        except Exception, e:
            m_error('Error en funcion  "request_get":\n')
            m_error('%s%s' % (PROPS['cursiva'], e), 0)

    def download_file(
            self, url, path_dest=None,
            spider=False, length_bar=50):
        """Funcion de descarga de archivo."""
        try:
            if os.path.exists(os.path.abspath(path_dest)):
                m_aviso('ya existe!!')
                return 1
            r = self.request_get(url, stream=True)
            if path_dest is None:
                if 'content-disposition' in r.headers.keys():
                    c_disposition = r.headers['content-disposition']
                    path_dest = c_disposition.split('filename=')[1][1:-1]
                else:
                    path_dest = url.split('/')[-1].split('?')[0]
            m_aviso('archivo: %s' % path_dest)
            if os.path.exists(os.path.abspath(path_dest)):
                m_aviso('ya existe!!')
                return 1
            else:
                m_aviso('guardando en %s' % path_dest)
            with open('%s' % path_dest, 'wb') as f:
                total_length=None
                dl=0
                if 'content-length' in r.headers.keys():
                  total_length = eval(r.headers.get('content-length'))
                  print "no content-length"
                  print '%s%s' % (PROPS['negrita'], fg_VERDE[1])
                if total_length is None:
                    for chunk in r.iter_content(1024):
                        dl += len(chunk)
                        f.write(chunk)
                        done = 0
                        sys.stdout.write(
                            "\r --" + "%" + " [%s%s] %s of %s" % (
                                '#' * done, '-' * (length_bar - done),
                                dl, "desconocido"))
                        sys.stdout.flush()
                    sys.stdout.write('\n')
                    print '%s' % END_char
                    m_aviso('guardando %s en %s\n' % (url, path_dest))
                else:
                    print '%s%s' % (PROPS['negrita'], fg_VERDE[1])
                    for chunk in r.iter_content(1024):
                        dl += len(chunk)
                        f.write(chunk)
                        percent = round(float(dl) * 100 / total_length, 2)
                        done = int(length_bar * dl / total_length)
                        sys.stdout.write(
                            "\r %s" % (percent) + "%" + " [%s%s] %s of %s" % (
                                '#' * done, '-' * (length_bar - done),
                                dl, total_length))
                        sys.stdout.flush()
                    sys.stdout.write('\n')
                    print '%s' % END_char
                if (dl / total_length == 1):
                    m_aviso('guardando %s en %s\n' % (url, path_dest))
                else:
                    m_aviso(
                        '%sDescarga incompleta\n eliminando%s' % (
                            PROPS['negrita'], END_char), 0)
                    os.remove(path_dest)
        except KeyboardInterrupt:
            print END_char
            m_aviso('%sCancelado por usuario\n eliminando%s' % (PROPS['negrita'],
                    END_char), 0)
            os.remove(path_dest)
            raise KeyboardInterrupt
        except Exception, e:
            print END_char
            m_error('Error en funcion "downloadFile":\n')
            m_error('%s%s' % (PROPS['cursiva'], e))
            m_error('\nEliminando')
            os.remove(path_dest)


    def download_from_file(self, path_orig):
        """Descarga desde enlaces guardados en archivo."""
        try:
            links = extras.extract_from_file(path_orig)
            m_aviso('Downloading %s files from %s' % (len(links), path_orig))
            for i in links:
                self.download_file(i)
        except:
            m_error('Surgio algun problema')
