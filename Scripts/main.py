import streamlit as st
import pandas as pd
import mysql.connector
st.set_page_config(page_title='CMS',page_icon='https://media.istockphoto.com/id/1165699436/vector/creative-workplace-with-computer-monitor-empty-no-people-cabinet-modern-office-furniture-flat.jpg?s=612x612&w=0&k=20&c=6OQYUj6XG_NNqwoaDdf2-L_mdTJQdu4D_xZrF7PHHOE=')
st.sidebar.title('MENU')
choice=st.sidebar.selectbox('My Menu',('Home','Admin Login'))  
st.sidebar.image('https://cdn.vectorstock.com/i/preview-1x/73/77/business-people-celebrating-victory-team-vector-29597377.jpg')
if(choice=='Home'): # Home
    st.markdown('<p style="font-family:serif; color:#FFFFFF;font-size:40px;text-align:center;text-decoration: underline;"><b>Welcome to Customer Management System 😊 </b></p>',unsafe_allow_html=True)
    st.image('https://cdn.dribbble.com/users/8619169/screenshots/16192755/media/188ce2fd1f246d546a189132510750e1.gif')
if(choice=='Admin Login'):  # Admin Login
    if 'login' not in st.session_state:
        st.session_state['login']=False
    if(not st.session_state['login']):
         st.markdown('<p style="font-family:serif; color:#FFFFFF;font-size:40px;text-align:center;text-decoration: underline;"><b>LOGIN PAGE </b></p>',unsafe_allow_html=True)
         st.markdown('<p style="font-family:serif; color:#FFFFFF;font-size:40px;text-align:center;text-decoration: underline;"><b>Fill Admin Details </b></p>',unsafe_allow_html=True)
         admid = st.text_input("Enter Admin ID: ")
         pwd = st.text_input("Enter Password: ")
         btn=st.button("Login")
         if btn:
             mydb=mysql.connector.connect(host="localhost",user="root",password="Adishi@26",database="customer")
             c=mydb.cursor()
             c.execute("select * from admin")
             for row in c:
                 if(row[0]==admid and row[1]==pwd):
                     st.session_state['login']=True
                     st.rerun()
                     st.header('Login Successfully 😊👍')
                     break
             if(not st.session_state['login']):
                 st.header('👎😓Wrong id or password \n Try again')
    if(st.session_state['login']):
        st.markdown('<p style="font-family:serif; color:#FFFFFF;font-size:40px;text-align:center;text-decoration: underline;"><b>DASHBOARD </b></p>',unsafe_allow_html=True)
        cc=st.selectbox(choice,('Overview','Add New Customer ',"View Customer Details",'Update Customer Details',"Delete Customer Details "))
        if(cc=='Overview'):
            st.image('https://img.freepik.com/premium-vector/secure-safety-online-guard-technology-security-verification-digital-check-software-internet-website-anti-virus-web-protection_212005-265.jpg')
        if(cc=='View Customer Details'):
            st.markdown('<p style="font-family:serif; color:#FFFFFF;font-size:40px;text-align:center;text-decoration: underline;"><b>Customer Details </b></p>',unsafe_allow_html=True)
            a=mysql.connector.connect(host='localhost',user='root',password='Adishi@26',database='customer')
            c=a.cursor()
            c.execute('select * from Customer')
            l=[]
            for i in c:
                l.append(i)
                df=pd.DataFrame(data=l,columns=c.column_names)
            st.image('https://t4.ftcdn.net/jpg/02/37/37/91/360_F_237379122_uhllhclrtGxvy4lOq1AtF4t8mcneQlTA.jpg')
            st.dataframe(df)
        if(cc=='Delete Customer Details '):
            st.markdown('<p style="font-family:serif; color:#FFFFFF;font-size:40px;text-align:center;text-decoration: underline;"><b>Delete Customer Details </b></p>',unsafe_allow_html=True)

            Id=st.text_input("Enter ID:-")
            a=mysql.connector.connect(host='localhost',user='root',password='Adishi@26',database='customer')
            b=a.cursor()
            b.execute('delete from Customer where id=%s',(Id,))
            a.commit()
            bt3=st.button('Remove')
            if bt3:
                st.header('Removed Successfully😊👍')
        if(cc=='Add New Customer '):
            cusid = st.text_input("Enter Customer ID: ")
            cufname = st.text_input("Enter Customer First Name: ")
            culname = st.text_input("Enter Customer Last Name: ")
            cugend = st.text_input("Enter Customer Gender: ")
            cuage = st.text_input("Enter Customer Age: ")
            cum = st.text_input("Enter Customer Marital Status:")
            cmail = st.text_input("Enter Customer Email:")
            cdob = st.text_input("Enter Customer DOB:")
            if st.button("Submit"):
                a=mysql.connector.connect(host='localhost',user='root',password='Adishi@26',database='customer')
                d=a.cursor()
                d.execute('insert into Customer values (%s,%s,%s,%s,%s,%s,%s,%s)',(cusid,cufname,culname,cugend,cuage,cum,cmail,cdob))
                a.commit()
                st.success("Customer added successfully!😊👍")
        if(cc=='Update Customer Details'):
            ch4=st.selectbox('Choose',('AGE','MARITAL_STATUS'))
            if(ch4=='AGE'):
                ID=st.number_input('ID:-')
                Age=st.number_input('Age:-')
                a=mysql.connector.connect(host='localhost',user='root',password='Adishi@26',database='customer')
                e=a.cursor()
                e.execute('update customer set age=%s where id=%s',(Age,ID))
                a.commit()
                bt3=st.button('Update')
                if bt3:
                    st.header('Age updated successfully!😊👍')
            else:
                ID=st.number_input('ID:-')
                mar=st.text_input('Marital_Status')
                a=mysql.connector.connect(host='localhost',user='root',password='Adishi@26',database='customer')
                e=a.cursor()
                e.execute('update customer set marital_status=%s where id =%s',(mar,ID))
                a.commit()
                bt3=st.button('Update')
                if bt3:
                    st.header('Marital_Status updated successfully!😊👍')

        

