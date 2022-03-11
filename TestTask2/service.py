import uuid

from models import db, Datasources

auth_type_guid = {
    'NoAuth':'e83a805b-0256-da61-ad0e-60a4580c3487',
    'ApiKey':'ccef14cb-ac0a-dd5d-1c2a-e3446d2312dd',
    'BearerToken':'43b5bcca-3e05-43d1-1661-e109fe8b331c',
    'BasicAuth':'c866422e-ab70-68d8-dccf-81b4a41319d5'
}

def featch_data_from_request(request):
    data = {}
    data["uuid_db"] = uuid.uuid4()
    data["description"] = request.form['description']
    data["enumname"] = request.form.get('enumname')
    data['ref_auth_type'] = auth_type_guid[f"{data['enumname']}"]
    data["httpaddress"] = request.form['httpaddress']
    data["apibaseurl"] = request.form['apibaseurl']
    data["apischemeurl"] = request.form['apischemeurl']
    data["marked"] = request.form.get('True')
    if type(data["marked"]) == str:
        data["marked"] = True
    else: data["marked"] = False

    if data['enumname'] == 'NoAuth':
        data["authorizationjson"] = ''
        data["autorizationtoken"] = ''
        data["autorizationlogin"] = ''
        data["autorizationpassword"] = ''
    
    if data['enumname'] == 'ApiKey':
        data["authorizationjson"] = request.form['authorizationjson']
        data["autorizationtoken"] = ''
        data["autorizationlogin"] = ''
        data["autorizationpassword"] = ''
    if data['enumname'] == 'BearerToken':
        data["authorizationjson"] = ''
        data["autorizationtoken"] = request.form['autorizationtoken']
        data["autorizationlogin"] = ''
        data["autorizationpassword"] = ''
    if data['enumname'] == 'BasicAuth':
        data["authorizationjson"] = ''
        data["autorizationtoken"] = ''
        data["autorizationlogin"] = request.form['autorizationlogin']
        data["autorizationpassword"] = request.form['autorizationpassword']
    
    return data


def insert(request):
    data = featch_data_from_request(request)
    datasource = Datasources(
            guid=data["uuid_db"],
            description=data["description"],
            ref_auth_type=data["ref_auth_type"],
            httpaddress=data["httpaddress"], 
            apibaseurl=data["apibaseurl"],
            apischemeurl=data["apischemeurl"],
            authorizationjson=data["authorizationjson"],
            autorizationlogin=data["autorizationlogin"],
            autorizationpassword=data["autorizationpassword"],
            autorizationtoken=data["autorizationtoken"],
            marked=data["marked"],
        )
    db.session.add(datasource)
    db.session.commit()

def update(request, guid):
    data = featch_data_from_request(request)
    datasource = Datasources.query.get(guid)

    datasource.description=data["description"]
    datasource.ref_auth_type=data["ref_auth_type"]
    datasource.httpaddress=data["httpaddress"],
    datasource.apibaseurl=data["apibaseurl"]
    datasource.apischemeurl=data["apischemeurl"]
    datasource.authorizationjson=data["authorizationjson"]
    datasource.autorizationlogin=data["autorizationlogin"]
    datasource.autorizationpassword=data["autorizationpassword"]
    datasource.autorizationtoken=data["autorizationtoken"]
    datasource.marked=data["marked"]
        
    db.session.commit()

def delete(guid):
    datasources = Datasources.query.get(guid)
    db.session.delete(datasources)
    db.session.commit()
