"""
\x1b[1m\x1b[93mcontiene colores y estilos
de muestreo y funciones de matizacion
de avisos \x1b[0m
"""


SPC_char = '\x1b'
END_char = '%s[0m' % SPC_char

PROPS = {
    'negrita': '%s[1m' % SPC_char,
    'debil': '%s[2m' % SPC_char,
    'cursiva': '%s[3m' % SPC_char,
    'subrayado': '%s[4m' % SPC_char,
    'resaltado': '%s[7m' % SPC_char,
    'resaltado_inv': '%s[8m' % SPC_char,
    'tachado': '%s[9m' % SPC_char
}

bg_NEGRO = ['%s[40m' % SPC_char, '%s[100m' % SPC_char]
bg_ROJO = ['%s[41m' % SPC_char, '%s[101m' % SPC_char]
bg_VERDE = ['%s[42m' % SPC_char, '%s[102m' % SPC_char]
bg_AMARILLO = ['%s[43m' % SPC_char, '%s[103m' % SPC_char]
bg_AZUL = ['%s[44m' % SPC_char, '%s[104m' % SPC_char]
bg_VIOLETA = ['%s[45m' % SPC_char, '%s[105m' % SPC_char]
bg_TURQUEZA = ['%s[46m' % SPC_char, '%s[106m' % SPC_char]
bg_GRIS = ['%s[47m' % SPC_char, '%s[107m' % SPC_char]


fg_NEGRO = ['%s[30m' % SPC_char, '%s[90m' % SPC_char]
fg_ROJO = ['%s[31m' % SPC_char, '%s[91m' % SPC_char]
fg_VERDE = ['%s[32m' % SPC_char, '%s[92m' % SPC_char]
fg_AMARILLO = ['%s[33m' % SPC_char, '%s[93m' % SPC_char]
fg_AZUL = ['%s[34m' % SPC_char, '%s[94m' % SPC_char]
fg_VIOLETA = ['%s[35m' % SPC_char, ' %s[95m' % SPC_char]
fg_TURQUEZA = ['%s[36m' % SPC_char, '%s[96m' % SPC_char]
fg_GRIS = ['%s[37m' % SPC_char, '%s[97m' % SPC_char]


print '%s%s%s al usar los colores recuerde usar el indice !!!! %s' % (
    fg_VERDE[1], PROPS['cursiva'], PROPS['negrita'], END_char)


def m_accion(cadena, opac=1):
    print '%s %s %s' % (
        fg_AZUL[opac], cadena, END_char)


def m_error(cadena, opac=1):
    print '%s%s %s %s' % (
        fg_ROJO[opac], PROPS['negrita'], cadena, END_char)


def m_interr(cadena, opac=1):
    print '%s%s %s %s' % (
        fg_AMARILLO[opac], PROPS['cursiva'], cadena, END_char)


def m_info(cadena, opac=1):
    print '%s %s %s' % (
        fg_VIOLETA[opac], cadena, END_char)


def m_aviso(cadena, opac=1):
    print '%s %s %s' % (
        fg_TURQUEZA[opac], cadena, END_char)


def m_dw(cadena, opac=0):
    print '%s %s %s' % (
        fg_GRIS[opac], cadena, END_char)
