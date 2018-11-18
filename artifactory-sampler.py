import requests

baseurl = 'http://ec2-18-191-200-247.us-east-2.compute.amazonaws.com:8081/artifactory/api/'

def print_response(response, format = 'json'):
    print(response.url)
    print(response)
    
    if format == 'plain':
        print(response.content)
    else:
        print(response.json())
        

def reload_plugins():
    reload_plugins_url = baseurl + 'plugins/reload'
    response = requests.post(reload_plugins_url, auth=('admin', 'm3lartifactory'))
    print_response(response, 'plain')


def get_build_info(build_name, build_number):
    build_info_url = baseurl + 'build/{buildname}/{buildnumber}'.format(buildname=build_name, buildnumber=build_number)
    response = requests.get(build_info_url, auth=('admin', 'm3lartifactory'))
    print_response(response)


def get_build_diff(build_name, build_number, old_build_number):
    urlparams = { 'diff' : old_build_number }
    get_build_diff_url = baseurl + 'build/{buildName}/{buildNumber}'.format(buildName=build_name, buildNumber=build_number)
    response = requests.get(get_build_diff_url, auth=('admin', 'm3lartifactory'), params = urlparams)
    print_response(response)

def checksum_search(checksums, repos = ''):
    urlparams = checksums
    if repos != '':
        urlparams['repos'] = repos

    build_info_url = baseurl + 'search/checksum'
    
    response = requests.get(build_info_url, auth=('admin', 'm3lartifactory'), params = urlparams)
    print_response(response)

def get_token():
    #gettokenurl = baseurl + 'security/token'
    print('not implemented')


userinput=''
while(userinput != 'q'):
    print('call REST:')
    print('1. reload plugins')
    print('2. get build info')
    print('3. get token') 
    print('4. get build diff')
    print('5. search checksum')
    print('q to quit')
    userinput = input('')

    if userinput == "1":
        reload_plugins()
    elif userinput == "2":
        get_build_info('somebuild', 1)
    elif userinput == "3":
        get_token()
    elif userinput == "4":
        get_build_diff('mybuild', 42, 41)
    elif userinput == "5":
        checksum_search({'sha256' : '67bcba1459185d718cf731a070324f12c06f411716af45f98b5a779c9bf5b471'}, 'nuget')
    elif userinput != "q":
        print('invalid selection')

    print('*******************************')

