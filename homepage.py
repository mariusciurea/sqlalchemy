"""SQLALCHEMY tutorial"""

import streamlit as st
from src.models import session, User

with st.sidebar:
    st.title("Save user data")

firstname = st.text_input("Input your firstname")
lastname = st.text_input("Input your lastname")
age = st.number_input("Input your age")
email = st.text_input("Input your email address")

submit = st.button("Submit")

if submit:
    # print(firstname)
    user = User(firstname=firstname, lastname=lastname, age=age, mail=email)
    session.add(user)
    session.commit()
    session.close()
    st.success("User added to db!")

users = session.query(User).all()
users_over_20 = session.query(User).filter(User.age > 20)
print(users_over_20)
for user in users_over_20:
    print(user.firstname, user.mail, user.age)