import pandas as pd
import numpy as np
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Evaluate the Mean Reciprocal Rank (MRR)@5')
    parser.add_argument('--gt_csv', type=str, required=True, help='Path to the ground truth CSV file')
    parser.add_argument('--pred_csv', type=str, required=True, help='Path to the prediction CSV file')
    return parser.parse_args()



def calculate_mrr_at_5(gt_csv, pred_csv):
    gt_df = pd.read_csv(gt_csv, header=None, names=['query_name', 'correct_output'])
    pred_df = pd.read_csv(pred_csv, header=None, names=['query_name', 'predictions'])
    
    reciprocal_ranks = []

    for _, gt_row in gt_df.iterrows():
        query_name = gt_row['query_name']
        correct_output = gt_row['correct_output']
        
        pred_row = pred_df[pred_df['query_name'] == query_name]
        if pred_row.empty:
            reciprocal_rank = 0
        
        predicted_outputs = pred_row.iloc[0]['predictions'].split(',')
        # print(predicted_outputs, gt_row)
        try:
            rank = predicted_outputs[:5].index(correct_output) + 1
            reciprocal_rank = 1 / rank
            
            # print(correct_output)
            # print(predicted_outputs)
            
        except ValueError as v:
            print(v)
            reciprocal_rank = 0
        # print()
        reciprocal_ranks.append(reciprocal_rank)
    
    print(reciprocal_ranks)
    
    # Calculate Mean Reciprocal Rank (MRR)@5
    mrr_at_5 = sum(reciprocal_ranks) / len(reciprocal_ranks)
    
    return mrr_at_5


if __name__ == '__main__':
    args = parse_args()
    mrr_at_5 = calculate_mrr_at_5(args.gt_csv, args.pred_csv)
    print(f'MRR@5: {mrr_at_5}')


