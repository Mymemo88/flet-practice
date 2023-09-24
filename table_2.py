import flet as ft
import sqlite3

def loutine(a):
    colm=ft.DataColumn(ft.Text(a))
    return colm

def get_db():
    dbdata=sqlite3.connect("stock.db")
    return dbdata


def main(page: ft.Page):
    con=get_db()
    cur=con.execute("select *, rowid from trade order by date desc;")
    data=cur.fetchall()
    con.close()
    datarow=[]
    for tmp in data:
        xx=[]
        xx=[loutine(tmp[0]),loutine(tmp[1]),loutine(tmp[2]),loutine(tmp[5])]
        datarow.append(ft.DataRow(xx))

    page.add(ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Day")),
            ft.DataColumn(ft.Text("Name")),
            ft.DataColumn(ft.Text("term"), numeric=True),
            ft.DataColumn(ft.Text("cost"),numeric=True),
            ],

        rows=datarow,
        
    ),
    )
    page.scroll="auto"
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER,port=5000)
