from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def reg(req):
    if req.method=='GET':
        return render(req,'reg.html')
    else:
        name=req.POST['name']
        email=req.POST['email']
        contact=req.POST['contact']
        uname=req.POST['uname']
        pswd=req.POST['pswd']
        print(name,email,contact)
        rg=Reg1()
        rg.name=name
        rg.email=email
        rg.mob=contact
        rg.username=uname
        rg.password=pswd
        rg.save()

        return redirect('login')
def loginuser(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        print(uname,pswd)
        # rg=Reg.objects.get(username=uname,password=pswd)
        # print(rg)
        try:
            rg=Reg1.objects.get(username=uname,password=pswd)
            print(rg)
            if rg:
                request.session['userid']=rg.id
                # return render(request,'loginpage.html')
                return redirect('details')
            else:
                return render(request,'login.html',{'msg':'invalid username and password'})
        except:
            return render(request,'login.html',{'msg':'invalid username and password'})
            
def emp_details(request):
    if 'userid' in request.session:
    
        if request.method=='GET':
            # try:
            ep=Emp1.objects.filter(uid_id=request.session['userid'])

                # ep=Emp1.objects.get(uid_id=req.session['userid'])
            return render(request,'emp_details.html',{'data':ep})
            # except:
            #     return render(request,'emp_details.html')

        else:
            ename=request.POST['ename']
            gender=request.POST['gender']
            age=request.POST['age']
            address=request.POST['addr']
            city=request.POST['city']
            dept=request.POST['dept']
            sal=request.POST['sal']
            
            print(ename,gender,age,address,city,dept,sal)
            ep=Emp1()
            ep.emp_name=ename
            ep.gender=gender
            ep.age=age
            ep.address=address
            ep.city=city
            ep.department=dept
            ep.salary=sal
            
            rg=Reg1.objects.get(id=request.session['userid'])
            ep.uid=rg
            ep.save()
        # dic1={'dept':dept,'sal':sal,'inc':inc}
            return redirect('details')
            
def editdata(request,id):
    if 'userid' in request.session:
        ep=Emp1.objects.get(pk=id)
    
        if request.method=='GET':
            print(id)
        
            return render(request,'edit.html',{'v':ep})
    
        else:
            uid=request.POST['uid']

            ep.emp_name=request.POST['ename']
            ep.gender=request.POST['gender'] 
            ep.age=request.POST['age']
            ep.address=request.POST['addr']
            ep.city=request.POST['city']
            ep.department=request.POST['dept']  
            ep.salary=request.POST['sal']
            # buyer=Emp1.objects.filter(id=uid)
    # buyer.update(name=name,gender=gender,address=address,dob=dob,country=country,username=username,password=password)
            ep.save()  
            return redirect('details')

def deletedata(request,id):
    if 'userid' in request.session:
        ep=Emp1.objects.get(pk=id)
        ep.delete()
        return redirect('details')
      