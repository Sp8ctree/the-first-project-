from os import path

def f(file, name, number):
    if not path.exists(f'files/{file}'):return "нет такого файла"
    a = [x for x in open(f'files/{file}') if '#' not in x]
    if not any(name in a[i] for i in range(len(a) - 1)):return "нет такого параметра"
    res = []
    r = ''
    for i in a:
        if 'name' in i:
            res.append(r)
            r = ''
            r = r + ' ' + i
        if 'name' not in i:
            r = r + ' ' + i

    masive_id = [x for x in res if name in x]
    return(masive_id[number-1])

while True:
    print('file = ac.ir; audio.ir; bluray_dvd.ir; digital_sing.ir; fans.ir; leds.ir; monitor.ir; projectors.ir;tv.ir')
    file = input("В каком файле ищем?")
    match file:
        case 'ac.ir':print('ac.ir = Off; Dh;Cool_hi; Cool_lo; Heat_hi; Heat_lo')
        case 'audio.ir':print('audio.ir = Power; Mute; Vol_up; Vol_dn; Play; Pause; Prev; Next')
        case 'bluray_dvd.i':print('audio.ir = Power; Mute; Vol_up; Vol_dn; Pause; Play; Prev; Next')
        case 'digital_sign.ir':print('digital_sign.ir = POWER; SOURCE; PLAY; STOP')
        case 'fans.ir':print('fans.ir = Power; Speed_up; Mode; Timer; Rotate; Speed_dn')
        case 'leds.ir':print('leds.ir = Power_on; Brightness_up; Brightness_dn; Power_off; Red; Green; Blue; White')
        case 'monitor.ir':print('monitor.ir = POWER; SOURCE; MENU; EXIT')
        case 'projector.ir':print('projector.ir = Power; Vol_up; Vol_dn; Mute; Play; Pause')
        case 'tv.ir':print('tv.ir = Power; Vol_up; Vol_dn; Ch_next; Ch_prev; Mute;')
    id = input("По какому критерию?")
    number = int(input("Номер"))
    print(f(file,id,number))
    input("Чтобы продолжить нажмите ENTER")