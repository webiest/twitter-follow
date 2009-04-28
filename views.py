import urllib2,base64
from django.utils import simplejson
from django.shortcuts import render_to_response
import forms
#import wingdbstub
import settings

def is_follows(follower, following):

    url = 'http://twitter.com/friendships/exists.json?user_a=%s&user_b=%s' %(
        follower, following)

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = "http://twitter.com/"
    password_mgr.add_password(None, top_level_url, settings.TWNAME, settings.TWPASSWORD)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(urllib2.HTTPHandler, handler)
    urllib2.install_opener(opener)
    
    try:
        return simplejson.load(urllib2.urlopen(url))
    except IOError, e:
        #print "Something wrong. This shouldnt happen"
        print e,"Protected user's details cant be found "
        return False

def format_is_follows(follower, following):
    fol = 'YES' if is_follows(follower,following) else 'NO'
    new_entry = (fol,follower,following)
    return "%s:%s:%s" %new_entry
        
def get_entry_tuples(str1="YES:str1:str2;NO:str3:str4"):
    list1 = str1.split(';')
    list2 = [tuple(i.split(":")) for i in list1]
    return list2
        
        
def disp(req):
    if req.method == 'POST':
        form = forms.input_form(req.POST)

        if form.is_valid():
            new_str = format_is_follows(form.cleaned_data['follower'],
                                        form.cleaned_data['following'])
            old_str = req.POST['old']
            
            form_data = "%s;%s" %(new_str,old_str)
            entries = get_entry_tuples(form_data)[:-1]
            
            payload = {'entries':entries,
                       'form':form,
                       'disp':True,
                       'form_data':form_data}
        else:
            payload = {'form':form,
                       'disp':True}
    else:
        form = forms.input_form()
        payload =  {'form':form,'disp':False}
    return render_to_response('page3.html',payload,)
    

if __name__=='__main__':
    #print is_follows('scobleizer','scorpion032')
    print get_old_entries().insert(0,('a','b'))