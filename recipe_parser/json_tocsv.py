#!/usr/bin/env python3

import pandas as pd
import json
import time
import ast
import ntpath

def load_DataFrame(input_file):
    df = pd.DataFrame(
        columns=["id", "name", "ingredients", "raw_ingredients", "directions", "labels", "servings", "domain", "host_url", "recipe_image", "total_time"])
    with open(input_file) as f:
        for i in f:
            df = df.append(json.loads(i), ignore_index=True)

    f.close()

    return df

def string_toList(row):
    output = []
    try:
        output = ast.literal_eval(row)
    except:
        output = output
    return output
def json_csv(input_file):
    # print(input_file)

    if ntpath.exists(str("D:/PyCharm_Projects/recipe-parser/output_files/") + input_file):
        file_name = str("D:/PyCharm_Projects/recipe-parser/output_files/") + input_file.split(".")[0].replace("_raw_recipies", "")
        recipes_file_name = file_name + str("_recipies.csv")
        ingredients_file_name = file_name + str("_ingredients.csv")
        raw_ingredients_file_name = file_name + str("_raw_ingredients.csv")
        directions_file_name = file_name + str("_instructions.csv")
    else:
        print("File Not Found")
        return OSError
    input_df = load_DataFrame("D:/PyCharm_Projects/recipe-parser/output_files/" + input_file)
    input_df.to_csv(recipes_file_name)
    #output_df = pd.DataFrame(columns=["labels", "ingredient", "amount", "unit", "descriptions"])
    ingredients_df_temp = input_df.loc[:, ["id", "ingredients"]].explode('ingredients')
    #output_df_temp['ingredients'] = output_df_temp['ingredients']
    raw_ingredients_df = input_df.loc[:,["id", "raw_ingredients"]].explode('raw_ingredients')
    directions_df = input_df.loc[:,["id", "directions"]].explode('directions')
    #output_df = output_df_temp.join(pd.json_normalize(output_df_temp.ingredients)).drop(columns=['ingredients'])
    ingredients_df = pd.concat([ingredients_df_temp['id'], ingredients_df_temp['ingredients'].apply(pd.Series)], axis = 1)






    ingredients_df.to_csv(ingredients_file_name, index = False)
    raw_ingredients_df.to_csv(raw_ingredients_file_name, index = False)
    directions_df.to_csv(directions_file_name, index = False)
    return None


if __name__ == "__main__":
    json_csv("re-run_400.json")


