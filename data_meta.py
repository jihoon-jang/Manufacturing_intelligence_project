from sqlalchemy.ext.declarative import declarative_base 
Base = declarative_base() 

from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, TIMESTAMP, DateTime, Float 

metadata2 =  MetaData() 

cnmeta_new = Table('tdata_30_IN', metadata2, 
               Column('id', Integer, primary_key=True),  
               Column('Serial', Integer), 
               Column('Rating', Integer), 
               Column('SOP', Float), 
               Column('LOR', Float), 
               Column('Research', Integer), 
               ) 
