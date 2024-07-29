import psycopg2 as pg

conn = pg.connect(
    host="localhost",
    database="pet_shop",
    user="postgres",
    password="682003"
)
cur=conn.cursor()
def list_pet():

  select_query="select * from pets;"
  cur.execute(select_query)
  records=cur.fetchall()
  pets_dict={}
  sales=[]
  pets=[]
  for r in records:
    pets_list =[('id',r[0]),('name',r[1]),('location',r[2]),('price',r[3])]
    pets.append(pets_list)


  for pet in pets:
    pets_dict={}
    for key,value in pet:
      pets_dict[key]=value
  
    sales.append(pets_dict)
  return sales


def listpet(id):
  select_query="select * from pets where id=(%s);"
  
  cur.execute(select_query,(id,))
  records=cur.fetchall()
  pets_dict={}
  result=[]
  pets=[]
  for r in records:
    pets_list =[('id',r[0]),('name',r[1]),('location',r[2]),('price',r[3])]
    pets.append(pets_list)


    pets_dict={}
    for key,value in pets_list:
      pets_dict[key]=value
  
    result.append(pets_dict)
  return result