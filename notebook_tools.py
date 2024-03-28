from IPython.display import display_html

###############################################
### QoL Tools for SQL and Jupyter Notebooks ###
###############################################

def side_by_side(df_dict:dict):
    html = ""
    for name, df in df_dict.items():
        html += df.style.set_table_attributes("style='display:inline; vertical-align:top;'").set_caption(name)._repr_html_()
    display_html(html, raw=True)

def get_sql_table_info(cursor, save_to_file=True, print_out=False) -> str | None:
    string = ""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        
        cursor.execute(f"PRAGMA table_info('{table_name}');")
        table_schema = cursor.fetchall()
        
        string += f"\n\nTable: {table_name}\nColumns:"
        
        string += "\n\tNAME                    "
        string += "TYPE         "
        string += "NOTNULL "
        string += "DEFAULT   "
        string += "PRIMARY KEY"
        
        for column in table_schema:
            string += f"\n\t{column[1]:<24}"
            string += f"{column[2]:<13}"
            string += f"{column[3]:<8}"
            string += f"{str(column[4]):<10}"
            string += f"{column[5]:<5}"
        
        # Check for foreign key constraints
        cursor.execute(f"PRAGMA foreign_key_list('{table_name}');")
        foreign_keys = cursor.fetchall()
        
        if foreign_keys:
            string += "\nForeign Key Constraints:"
            string += f"\n\tCOLUMN{'':<18}REFERENCES"
            for fk in foreign_keys:
                string += f"\n\t{fk[3]:<24}" + f"{fk[2]}.{fk[4]}"

    if print_out:
        print(string)
    
    if save_to_file:
        with open("table_info.txt", "w") as f:
            f.write(string)
    
    return string