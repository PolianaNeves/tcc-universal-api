from models.attractions import ReviewsCountAttractionsByBranch
from models.reviews import ReviewsCountBy
from inits.init_dataset import dataset_attractions_count

def count_reviews_by_attraction():
    branch_list = ["full", "florida", "japan", "singapore"]
    label_list = ["all", "pos", "neg"]
    list_branches = []
    for branch in branch_list:
        name_list = []
        count_list = []
        for label in label_list:
            column_filter = f'{branch}_count'
            if label != "all":
                column_filter = f'{branch}_count_{label}'
            name = f'{column_filter}_name'
            name_list.append(name)
            count_list.append(column_filter)
        df_filtered_branch = dataset_attractions_count
        list_attractions = []
        for attraction in df_filtered_branch[df_filtered_branch[name_list[0]].notnull()][name_list[0]]:
            filtered_total = df_filtered_branch[(df_filtered_branch[name_list[0]].notnull()) & (df_filtered_branch[name_list[0]] == attraction)]
            total_count = filtered_total[count_list[0]] if len(filtered_total) > 0 else 0
            filtered_pos = df_filtered_branch[(df_filtered_branch[name_list[1]].notnull()) & (df_filtered_branch[name_list[1]] == attraction)]
            pos_count = filtered_pos[count_list[1]] if len(filtered_pos) > 0 else 0
            filtered_neg = df_filtered_branch[(df_filtered_branch[name_list[2]].notnull()) & (df_filtered_branch[name_list[2]] == attraction)]
            neg_count = filtered_neg[count_list[2]] if len(filtered_neg) > 0 else 0
            list_attractions.append(ReviewsCountBy(label=attraction, total=int(total_count), positive=int(pos_count), negative=int(neg_count)))
        list_branches.append(ReviewsCountAttractionsByBranch(branch=branch, data=list_attractions))
    return list_branches
