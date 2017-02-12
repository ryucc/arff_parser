import sys
import re
'''
    ARFF OBJECT:
            'description': '',
            'relation': name of relation,
            'attributes': ['arr1':{},att2,att3,...],
            'data': [arr1,att2,att3,...],
'''
def parse_arff(filename):
    aaa = open(filename)
    obj = {
            'description': '',
            'relation': '',
            'attributes': [],
            'data': [],
            }
    line = aaa.readline()
    while line:
        if line[0] == '%':
            line = aaa.readline()
            continue
        p = line.split()
        if p[0].upper() == '@RELATION':
            obj['relation'] = p[1];
        elif p[0].upper() == '@ATTRIBUTE':
            natt = [re.sub(',| |{|}','',x) for x in p[3:]]
            while '' in natt:
                natt.remove('')
            obj['attributes'].append((re.sub("'",'',p[1]),natt))
        elif p[0].upper() == '@DATA':
            line = aaa.readline()
            break;
        line = aaa.readline()
    while line:
        line = line[:-1]
        dt = re.split('\n|,',line)
        while '' in dt:
            dt.remove('')
        obj['data'].append(dt)
        line = aaa.readline()
    return obj
