import sys
import pandas as pd

def main():
    args = sys.argv
    df = pd.read_csv(args[1])
    
    #リスト型で取得
    player_id = df['player_id'].unique()
    
    #key-player_id, value-player_score.mean()
    player_dict = {}
    for i, v in enumerate(player_id):
        player_score = [df[df['player_id'] == v].mean()]
        
        player_dict[player_id[i]] = player_score[0][0]

    #辞書型をvalueをもとに降順ソート
    sorted_player_dict = sorted(player_dict.items(), key=lambda x: x[1], reverse=True)

    #データフレームを作成するためのid配列とscore配列を用意
    sorted_id = []
    sorted_score = []
    for j, k in enumerate(sorted_player_dict):
        sorted_id.append(k[0])
        sorted_score.append(k[1])

    #辞書型にしてデータフレーム作成
    sorted_dict = dict(player_id=sorted_id, mean_score=sorted_score)
    sorted_df = pd.DataFrame(data=sorted_dict)

    #rank列を作成
    sorted_df['rank'] = sorted_df['mean_score'].rank(ascending=0)
    print(sorted_df)

if __name__ =="__main__":
    main()
