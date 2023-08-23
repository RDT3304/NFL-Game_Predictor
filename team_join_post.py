import pandas as pd

def update_team_abbreviations(merged_data_path, nfl_teams_path, output_path):
    # Read the merged data file
    merged_data_df = pd.read_csv(merged_data_path)

    # Read the NFL teams file
    nfl_teams_df = pd.read_csv(nfl_teams_path)

    # Remove leading and trailing whitespace from team names and abbreviations
    nfl_teams_df['Name'] = nfl_teams_df['Name'].str.strip()
    nfl_teams_df['Abbreviation'] = nfl_teams_df['Abbreviation'].str.strip()
    merged_data_df['Team'] = merged_data_df['Team'].str.strip()

    # Create a dictionary to map the old abbreviations to the new ones
    abbreviation_mapping = dict(zip(nfl_teams_df['Name'], nfl_teams_df['Abbreviation']))

    # Update the 'Team' column in the merged data using the mapping
    merged_data_df['Team'] = merged_data_df['Team'].map(abbreviation_mapping)

    # Save the updated merged data to a new CSV file
    merged_data_df.to_csv(output_path, index=False)

    return f"Updated file saved to {output_path}"


update_team_abbreviations('post season data/merged_data_def_off_st_post.csv', 'Original Data/nfl_teams.csv', 'post season data/updated_merged_data.csv')


import pandas as pd

def add_win_column(nfl_schedule_path, merged_data_path, output_path):
    # Read the NFL schedule file
    nfl_schedule_df = pd.read_csv(nfl_schedule_path)

    # Read the merged data file
    merged_data_df = pd.read_csv(merged_data_path)

    # Create a dictionary to hold the winning information
    win_dict = {}
    for index, row in nfl_schedule_df.iterrows():
        winner_team = row['Winner/tie']
        loser_team = row['Loser/tie']
        week = row['Week']
        win_dict[(winner_team, week)] = 1
        win_dict[(loser_team, week)] = 0

    # Create a 'Win' column in the merged data
    merged_data_df['Win'] = merged_data_df.apply(lambda row: win_dict.get((row['Team'], row['Week']), None), axis=1)

    # Save the updated merged data to a new CSV file
    merged_data_df.to_csv(output_path, index=False)

    return f"Updated file saved to {output_path}"

# Example usage
add_win_column('NFL_schedule_results_2022_post_updated.csv', 'merged_data_def_off_st_post.csv', 'output_file.csv')

# Count the total number of NaN values in the entire dataframe
total_nans = data_df.isna().sum().sum()

# Initialize a counter for NaNs preceded by zeros in the two columns before the NaN
nans_preceded_by_zeros = 0

# Iterate through the dataframe to find NaNs preceded by zeros in the two columns before the NaN
for i in range(data_df.shape[0]):
    for j in range(2, data_df.shape[1]):
        if pd.isna(data_df.iloc[i, j]) and data_df.iloc[i, j - 1] == 0 and data_df.iloc[i, j - 2] == 0:
            nans_preceded_by_zeros += 1

total_nans, nans_preceded_by_zeros
