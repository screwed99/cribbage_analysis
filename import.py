import pandas as pd
import numpy as np

def load_game_to_dataframe(relative_file_path):
    df = pd.read_csv(relative_file_path,
                     header=0,
                     names=["Game","Deal","Position","Player","Play Points","Broken Down Play Points","Show Points",
                            "Crib Points","Missed Points","Won in Play","Won in Show"],
                     dtype={"Game": np.int64,"Deal": np.int64,"Position": np.object,"Player": np.object,
                            "Play Points": np.int64,"Broken Down Play Points": np.object,"Show Points": np.object,
                            "Crib Points": np.object,"Missed Points": np.object,"Won in Play": np.int64,
                            "Won in Show": np.int64},
                     na_values="NULL")
    return df

df = load_game_to_dataframe("game_1.csv")
print(df.head())
print(df.dtypes)
print(df['Show Points'])