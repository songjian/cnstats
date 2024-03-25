from .common import easyquery

def get_tree(id='zb', dbcode='hgyd'):
    for n in easyquery(m='getTree', dbcode=dbcode, wdcode='zb', id=id):
        print(n['id'], n['name'])
        if n['isParent']: get_tree(n['id'], dbcode)

if __name__ == '__main__':
    get_tree('zb')