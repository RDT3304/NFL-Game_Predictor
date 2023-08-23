import pandas as pd

# Loading the files
def_passing_df = pd.read_csv('Original Data/Def_Passing_2022_reg.csv')
def_receiving_df = pd.read_csv('Original Data/Def_Receiving_2022_reg.csv')
def_rushing_df = pd.read_csv('Original Data/Def_Rushing_2022_reg.csv')

# Merging defensive passing and receiving dataframes
merged_df_1 = pd.merge(def_passing_df, def_receiving_df, on=['Team', 'Week'], suffixes=('_pass', '_rec'))

# Merging the resulting dataframe with defensive rushing dataframe
def_final_merged_df = pd.merge(merged_df_1, def_rushing_df, on=['Team', 'Week'], suffixes=('', '_rush'))

# Path to save the final merged CSV
output_path = 'C:\\Users\\ramon\\Python Coding\\Personal Projects\\NFL\\reg season data\\merged_data_def.csv'

# Saving the final merged dataframe as a CSV file
def_final_merged_df.to_csv(output_path, index=False)

# Loading the newly uploaded files into separate dataframes
passing_reg_df = pd.read_csv('Original Data/Passing_2022_reg.csv')
receiving_reg_df = pd.read_csv('Original Data/Receiving_2022_reg.csv')
rushing_reg_df = pd.read_csv('Original Data/Rushing_2022_reg.csv')

# Merging passing and receiving dataframes
off_final_merged_df = pd.merge(passing_reg_df, receiving_reg_df, on=['Team', 'Week'], suffixes=('_pass', '_rec'))

# Merging the resulting dataframe with rushing dataframe
off_final_merged_df = pd.merge(off_final_merged_df, rushing_reg_df, on=['Team', 'Week'], suffixes=('', '_rush'))

# Path to save the final merged CSV for reg data
output_reg_path = 'C:\\Users\\ramon\\Python Coding\\Personal Projects\\NFL\\reg season data\\merged_data_off.csv'

# Saving the final merged dataframe as a CSV file
off_final_merged_df.to_csv(output_reg_path, index=False)

# Loading the newly uploaded special teams files into separate dataframes
st_kicking_reg_df = pd.read_csv('Original Data/ST_Kicking_2022_reg.csv')
st_punt_reg_df = pd.read_csv('Original Data/ST_Punt_2022_reg.csv')
st_return_reg_df = pd.read_csv('Original Data/ST_Return_2022_reg.csv')

# Merging kicking and punt dataframes
merged_st_reg_df_1 = pd.merge(st_kicking_reg_df, st_punt_reg_df, on=['Team', 'Week'], suffixes=('_kicking', '_punt'))

# Merging the resulting dataframe with return dataframe
st_final_merged_df = pd.merge(merged_st_reg_df_1, st_return_reg_df, on=['Team', 'Week'], suffixes=('', '_return'))

# Path to save the final merged CSV for special teams reg data
output_st_reg_path = 'C:\\Users\\ramon\\Python Coding\\Personal Projects\\NFL\\reg season data\\merged_data_st.csv'

# Saving the final merged dataframe as a CSV file
st_final_merged_df.to_csv(output_st_reg_path, index=False)

# Loading the newly uploaded merged files into separate dataframes
merged_def_data_reg_df = pd.read_csv('reg season data/merged_data_def.csv')
merged_off_data_reg_df = pd.read_csv('reg season data/merged_data_off.csv')
merged_st_data_reg_df = pd.read_csv('reg season data/merged_data_st.csv')

# Merging the merged defense, offense, and special teams dataframes on 'Team' and 'Week' columns
# Merging defense and offense dataframes
merged_def_off_reg_df = pd.merge(merged_def_data_reg_df, merged_off_data_reg_df, on=['Team', 'Week'], suffixes=('_def', '_off'))

# Merging the resulting dataframe with special teams dataframe
final_merged_def_off_st_reg_df = pd.merge(merged_def_off_reg_df, merged_st_data_reg_df, on=['Team', 'Week'], suffixes=('', '_st'))

# Path to save the final merged CSV for defense, offense, and special teams reg data
output_def_off_st_reg_path = 'C:\\Users\\ramon\\Python Coding\\Personal Projects\\NFL\\reg season data\\merged_data_def_off_st_reg.csv'

# Saving the final merged dataframe as a CSV file
final_merged_def_off_st_reg_df.to_csv(output_def_off_st_reg_path, index=False)

# Displaying the first few rows of the final merged dataframe for defense, offense, and special teams reg data
final_merged_def_off_st_reg_df.head(), output_def_off_st_reg_path


