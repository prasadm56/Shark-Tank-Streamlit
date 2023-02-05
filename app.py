import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from PIL import Image
import streamlit.components.v1 as components  # Import Streamlit




st.set_page_config(layout='wide')

dff=pd.read_csv('Shark_Tank_India_S1.csv')
col=['episode_number','startup_number', 'brand_name','domain', 'description','deal_amount_lakhs','aman_invested','anupam_invested', 
       'ashneer_invested',  'ghazal_invested','namita_invested', 'peyush_invested',  'vineeta_invested',
       'amount_per_shark', 'equity_per_shark']
ndf=dff[col]

st.components.v1.html(
    """
    <div style="color:white;text-align:center;"white-space:nowrap;"">
    	<h1 >Shark  Tank India S1 🦈</h1>
        
    </div>
    """,
    width=1500,
    height=100
)


col1=st.columns(1)

#st.header('Shark Tank India S1 :shark:')
image = Image.open('st.png')
st.image(image, caption='Shark Tank India S1',width=1400)

list_of_shark = ["Aman Gupta","Ashneer Grover","Anupam Mittal","Ghazal Alagh","Namita Thapar","Peyush Bansal","Vineeta Singh"]
list_of_shark.insert(0,'All Sharks')



#plot = st.sidebar.button('Plot Graph')

col1, col2, col3, col4, col5, col6,col7= st.columns(7)

with col5:
   #st.header("Aman Gupta")
   image = Image.open('aman.png')

   st.image(image, caption='Aman Gupta',width=190)
   #st.write("")
   st.components.v1.html(
    """
    <div style="color:white;text-align:center;">
    	<h4>Co-founder and Chief Marketing Officer of boAt</h4>
        <h4>Investment</h4>
        <h2 style="color:lime">₹9.36Cr</h2>
        <h4>Number of Deals</h4>
        <h2 style="color:lime">28</h2>
    </div>
    """,
    width=175,
    height=300
)
   aman=st.button("Aman's Investments")

with col4:
   #st.header("Ashneer Grover",)
   image = Image.open('ashneer.png')
   st.image(image, caption='Ashneer Grover',width=190)
  #former co-founder and managing director (MD) of the Indian fintech company BharatPe
   #st.write("Former co-founder and managing director of BharatPe")
   #st.metric(label="Investment", value="₹5.39Cr")
   #st.metric(label="Number of Deals", value="21")
   
   st.components.v1.html(
    """
    <div style="color:white;text-align:center;">
    	<h4>Former co-founder and managing director of BharatPe</h4>
        <h4>Investment</h4>
        <h2 style="color:lime">₹5.39Cr</h2>
        <h4>Number of Deals</h4>
        <h2 style="color:lime">21</h2>
    </div>
    """,
    width=175,
    height=300
)
   ashneer=st.button("Ashneer's Investments")
   

with col7:
   #st.header("Anupam Mittal")
   image = Image.open('anupam.png')
   st.image(image, caption='Anupam Mittal', width=190)
   st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
    	<h4>Founder and CEO of Shaadi.com and People Group</h4>
        <h4>Investment</h4>
        <h2 style="color:lime">₹5.39Cr</h2>
        <h4>Number of Deals</h4>
        <h2 style="color:lime">24</h2>
    </div>
    """,
    width=175,
    height=300
)
   #ashneer=st.button("Anupam's Investments")
   anupam=st.button("Anupam's Investments")


with col2:
   #st.header("Peyush Bansal")
   image = Image.open('peyush.png')
   st.image(image, caption='Peyush Bansal', width=190)
 
   st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
    	<h3>Co-founder and Chief Executive Officer of Lenskart</h3>
        <h4>Investment</h4>
        <h2 style="color:lime">₹8.3Cr</h2>
        <h4>Number of Deals</h4>
        <h2 style="color:lime">24</h2>
    </div>
    """,
    width=175,
    height=300
)

   peyush=st.button("Peyush's Investments")


with col6:
   #st.header("Namita Thapar")
   image = Image.open('Namitha.png')
   st.image(image, caption='Namita Thapar', width=190)
   st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
    	<h4>Executive Director of Emcure Pharmaceuticals</h4>
        <h4>Investment</h4>
        <h2 style="color:lime">₹6.38Cr</h2>
        <h4>Number of Deals</h4>
        <h2 style="color:lime">22</h2>
    </div>
    """,
    width=175,
    height=300
)

   namita=st.button("Namita's Investments")

with col1:
    #st.header(" Vineeta Singh")
    image = Image.open('Vineta.png')
    st.image(image, caption='Vineeta Singh', width=190)
    st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
    	<h3>CEO and co-founder of SUGAR Cosmetics</h3>
        <h4>Investment</h4>
        <h2 style="color:lime">₹3.04Cr</h2>
        <h4>Number of Deals</h4>
        <h2 style="color:lime">22</h2>
    </div>
    """,
    width=175,
    height=300
)

    vineeta=st.button("Vineeta's Investments")

with col3:
    #st.header("Ghazal Alagh")
    image = Image.open('ghazal.png')
    st.image(image, caption='Ghazal Alagh', width=190)
    st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
    	<h3>Co-founder and Chief Mama of MamaEarth </h3>
		<h4>Investment</h4>
        <h2 style="color:lime">₹1.2Cr</h2>
        <h4>Number of Deals</h4>
        <h2 style="color:lime">7</h2>
    </div>
    """,
    width=175,
    height=300
)

    ghazal=st.button("Ghazal's Investments")


    
    

col1=st.columns(1)
if aman==True:
    amandf=ndf[ndf['aman_invested']==1]
    fig = px.bar(amandf, x=amandf['brand_name'], y=amandf['amount_per_shark'],title="Aman's Equity Investment",color=amandf['domain'],
                 labels={'amount_per_shark':'Amount Invested in Lacs(₹)','brand_name': 'Invested Brand Name','domain':'Domain','equity_per_shark':"Aman's Equity(%)"},
                 hover_data=['equity_per_shark'])
    st.plotly_chart(fig, use_container_width=True)
    st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
         <p>
        <mark>Explore Domain Contributions by clicking on a specific Domain</mark> 
    </p>
 
    </div>
    """,
    width=1370,
    height=50
)
    #st.dataframe(amandf,use_container_width=True)
    fig2=px.sunburst(amandf,path=['domain','brand_name'],values='amount_per_shark',height=700,width=700,
            labels={'amount_per_shark':"Aman's investments in Lacs(₹)",'labels':'Company Name','parent':"Domain",'id':'Subdomain'},title="Aman's Domain specific investments")
    st.plotly_chart(fig2, use_container_width=True)

                    

col1=st.columns(1)    
if ashneer==True:
    ashneerdf=ndf[ndf['ashneer_invested']==1]
    fig = px.bar(ashneerdf, x=ashneerdf['brand_name'], y=ashneerdf['amount_per_shark'],title="Ashneer's Equity Investment",color=ashneerdf['domain'],
                 labels={'brand_name': 'Invested Brand Name','amount_per_shark':'Amount Invested in Lacs(₹)','domain':'Domain',
                 'equity_per_shark':"Ashneer's Equity(%)"},
                 hover_data=['equity_per_shark'])
    st.plotly_chart(fig, use_container_width=True)
    #st.dataframe(ashneerdf,use_container_width=True)
    st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
         <p>
        <mark>Explore Domain Contributions by clicking on a specific Domain</mark> 
    </p>
 
    </div>
    """,
    width=1370,
    height=50
)

    fig2=px.sunburst(ashneerdf,path=['domain','brand_name'],values='amount_per_shark',height=700,width=700,
            labels={'amount_per_shark':"Ashneer's investments in Lacs(₹)",'labels':'Company Name','parent':"Domain",'id':'Subdomain'},title="Ashneer's Domain specific investments")
    st.plotly_chart(fig2, use_container_width=True)
    
    
col1=st.columns(1)    
if peyush==True:
    peyushdf=ndf[ndf['peyush_invested']==1]
    fig = px.bar(peyushdf, x=peyushdf['brand_name'], y=peyushdf['amount_per_shark'],title="Aman's Equity Investment",color=peyushdf['domain'],
                 labels={'brand_name': 'Invested Brand Name','amount_per_shark':'Amount Invested in Lacs(₹)','domain':'Domain','equity_per_shark':"Peyush's Equity(%)"},
                 hover_data=['equity_per_shark'])
    st.plotly_chart(fig, use_container_width=True)
    st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
         <p>
        <mark>Explore Domain Contributions by clicking on a specific Domain</mark> 
    </p>
 
    </div>
    """,
    width=1370,
    height=50
)

    fig2=px.sunburst(peyushdf,path=['domain','brand_name'],values='amount_per_shark',height=700,width=700,
            labels={'amount_per_shark':"Peyush's investments in Lacs(₹)",'labels':'Company Name','parent':"Domain",'id':'Subdomain'},title="Peyush's Domain specific investments")
    st.plotly_chart(fig2, use_container_width=True)
    
    
col1=st.columns(1)    
if namita==True:
    namitadf=ndf[ndf['namita_invested']==1]
    fig = px.bar(namitadf, x=namitadf['brand_name'], y=namitadf['amount_per_shark'],title="Namita's Equity Investment",color=namitadf['domain'],
                 labels={'brand_name': 'Invested Brand Name','amount_per_shark':'Amount Invested in Lacs(₹)','domain':'Domain','equity_per_shark':"Namita's Equity(%)"},
                 hover_data=['equity_per_shark'])
    st.plotly_chart(fig, use_container_width=True)
    st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
         <p>
        <mark>Explore Domain Contributions by clicking on a specific Domain</mark> 
    </p>
 
    </div>
    """,
    width=1370,
    height=50
)

    fig2=px.sunburst(namitadf,path=['domain','brand_name'],values='amount_per_shark',height=700,width=700,
            labels={'amount_per_shark':"Namita's investments in Lacs(₹)",'labels':'Company Name','parent':"Domain",'id':'Subdomain'},title="Namita's Domain specific investments")
    st.plotly_chart(fig2, use_container_width=True)
    
col1=st.columns(1)    
if ghazal==True:
    ghazaldf=ndf[ndf['ghazal_invested']==1]
    fig = px.bar(ghazaldf, x=ghazaldf['brand_name'], y=ghazaldf['amount_per_shark'],title="Ghazal's Equity Investment",color=ghazaldf['domain'],
                 labels={'brand_name': 'Invested Brand Name','amount_per_shark':'Amount Invested in Lacs(₹)','domain':'Domain','equity_per_shark':"Ghazal's Equity(%)"},
                 hover_data=['equity_per_shark'])
    st.plotly_chart(fig, use_container_width=True)
    st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
         <p>
        <mark>Explore Domain Contributions by clicking on a specific Domain</mark> 
    </p>
 
    </div>
    """,
    width=1370,
    height=50
)

    fig2=px.sunburst(ghazaldf,path=['domain','brand_name'],values='amount_per_shark',height=700,width=700,
            labels={'amount_per_shark':"Ghazal's investments in Lacs(₹)",'labels':'Company Name','parent':"Domain",'id':'Subdomain'},title="Ghazal's Domain specific investments")
    st.plotly_chart(fig2, use_container_width=True)
    
    
col1=st.columns(1)    
if vineeta==True:
    vineetadf=ndf[ndf['vineeta_invested']==1]
    fig = px.bar(vineetadf, x=vineetadf['brand_name'], y=vineetadf['amount_per_shark'],title="Vineeta's Equity Investment",color=vineetadf['domain'],
                 labels={'brand_name': 'Invested Brand Name','amount_per_shark':'Amount Invested in Lacs(₹)','domain':'Domain','equity_per_shark':"Vineeta's Equity(%)"},
                 hover_data=['equity_per_shark'])
    st.plotly_chart(fig, use_container_width=True)
    st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
         <p>
        <mark>Explore Domain Contributions by clicking on a specific Domain</mark> 
    </p>
 
    </div>
    """,
    width=1370,
    height=50
)

    fig2=px.sunburst(vineetadf,path=['domain','brand_name'],values='amount_per_shark',height=700,width=700,
            labels={'amount_per_shark':"Vineeta's investments in Lacs(₹)",'labels':'Company Name','parent':"Domain",'id':'Subdomain'},title="Vineeta's Domain specific investments")
    st.plotly_chart(fig2, use_container_width=True)
    
    
col1=st.columns(1)    
if anupam==True:
    anupamdf=ndf[ndf['anupam_invested']==1]
    fig = px.bar(anupamdf, x=anupamdf['brand_name'], y=anupamdf['amount_per_shark'],title="Anupam's Equity Investment",color=anupamdf['domain'],
                 labels={'brand_name': 'Invested Brand Name','amount_per_shark':'Amount Invested in Lacs(₹)','domain':'Domain','equity_per_shark':"Anupam's Equity(%)"},
                 hover_data=['equity_per_shark'])
    st.plotly_chart(fig, use_container_width=True)
    st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
         <p>
        <mark>Explore Domain Contributions by clicking on a specific Domain</mark> 
    </p>
    <h1 style="color: green;">Anupam's Domain specific investments </h1>
 
    </div>
    
    """,
    width=1370,
    height=50
)

    fig2=px.sunburst(anupamdf,path=['domain','brand_name'],values='amount_per_shark',height=700,width=700,
            labels={'amount_per_shark':"Anupam's investments in Lacs(₹)",'labels':'Company Name','parent':"Domain",'id':'Subdomain'},title="Anupam's Domain specific investments")
    st.plotly_chart(fig2, use_container_width=True)
    
ndf['ashneer_True']=ndf['ashneer_invested'].replace({1:'Ashneer'})
ndf['aman_True']=ndf['aman_invested'].replace({1:'Aman'})
ndf['anupam_True']=ndf['anupam_invested'].replace({1:'Anupam'})
ndf['namita_True']=ndf['namita_invested'].replace({1:'Namita'})
ndf['ghazal_True']=ndf['ghazal_invested'].replace({1:'Ghazal'})
ndf['vineeta_True']=ndf['vineeta_invested'].replace({1:'Vineeta'})
ndf['peyush_True']=ndf['peyush_invested'].replace({1:'Peyush'})


# Melt the data frame to have each shark as a separate row
df_melted = ndf.melt(id_vars=['brand_name', 'deal_amount_lakhs','domain','equity_per_shark'], value_vars=['ashneer_True', 'aman_True', 'anupam_True',
                                                              'namita_True', 'ghazal_True', 'vineeta_True', 'peyush_True'], value_name='shark_name')

# Filter out rows where shark_name is 0 (no investment)
df_melted = df_melted[df_melted['shark_name'] != 0]


columns = st.columns((2, 1, 2))
button_pressed = columns[1].button('All Sharks investments!')


if button_pressed==True:
    close=columns[2].button("close chart")
    st.components.v1.html(
	"""
    <div style="color:white;text-align:center;">
         <p>
        <mark>Click on the shark name to view the individual investment amount made by each shark</mark> 
    </p>
    <h1 style="color: green;">Anupam's Domain specific investments </h1>
 
    </div>
    
    """,
    width=1370,
    height=50
)
    #df_melted = df_melted.assign(domain = pdf.loc[df_melted['brand_name'].index, 'domain'])
    fig = px.bar(df_melted, x='brand_name', y='deal_amount_lakhs', color='shark_name', width=1000, height=700, text_auto=True, hover_data=['domain','equity_per_shark'],
             labels={'brand_name': 'Invested Brand Name','deal_amount_lakhs':'Amount by shark/sharks Invested in Lacs(₹)',
                     'shark_name':'Shark Name','equity_per_shark':"Shark's Equity",'domain':'Domain'},title='All Shark Tank Investment Summary')

    st.plotly_chart(fig, use_container_width=True)
#st.button("close")
