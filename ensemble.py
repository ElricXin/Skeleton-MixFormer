import argparse
import pickle
import os

import numpy as np
from tqdm import tqdm
from skopt import gp_minimize

def objective(weights):
    right_num = total_num = 0
    for i in tqdm(range(len(label))):
        l = label[i]
        _, r11 = r1[i]
        _, r22 = r2[i]
        _, r33 = r3[i]
        _, r44 = r4[i]
        _, r55 = r5[i]
        _, r66 = r6[i]
        
        r = r11 * weights[0] + r22 * weights[1] + r33 * weights[2] + r44 * weights[3] + r55 * weights[4] + r66 * weights[5]
        r = np.argmax(r)
        right_num += int(r == int(l))
        total_num += 1
    acc = right_num / total_num
    print(acc)
    return -acc  # We want to maximize accuracy, hence minimize -accuracy


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset',
                        required=True,
                        choices={'ntu/xsub', 'ntu/xview', 'ntu120/xsub', 'ntu120/xset', 'NW-UCLA'},
                        help='the work folder for storing results')
    parser.add_argument('--alpha',
                        default=1,
                        help='weighted summation',
                        type=float)

    parser.add_argument('--joint-dir',
                        help='Directory containing "epoch1_test_score.pkl" for joint eval results')
    parser.add_argument('--bone-dir',
                        help='Directory containing "epoch1_test_score.pkl" for bone eval results')
    parser.add_argument('--joint-motion-dir', default=None)
    parser.add_argument('--bone-motion-dir', default=None)
    parser.add_argument('--joint-k2-dir', default=None)
    parser.add_argument('--joint-motion-k2-dir', default=None)

    arg = parser.parse_args()

    dataset = arg.dataset
    if 'UCLA' in arg.dataset:
        label = []
        with open('./data/' + 'NW-UCLA/' + '/val_label.pkl', 'rb') as f:
            data_info = pickle.load(f)
            for index in range(len(data_info)):
                info = data_info[index]
                label.append(int(info['label']) - 1)
    elif 'ntu120' in arg.dataset:
        if 'xsub' in arg.dataset:
            npz_data = np.load('./data/' + 'ntu120/' + 'NTU120_CSub.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
        elif 'xset' in arg.dataset:
            npz_data = np.load('./data/' + 'ntu120/' + 'NTU120_CSet.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
    elif 'ntu' in arg.dataset:
        if 'xsub' in arg.dataset:
            npz_data = np.load('./data/' + 'ntu/' + 'NTU60_CS.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
        elif 'xview' in arg.dataset:
            npz_data = np.load('./data/' + 'ntu/' + 'NTU60_CV.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
    elif 'uav' in arg.dataset:
        if 'csv1' in arg.dataset:
            npz_data = np.load('./data/' + 'uav/' + 'UAV_csv1.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
        elif 'scv2' in arg.dataset:
            npz_data = np.load('./data/' + 'uav/' + 'UAV_csv2.npz')
            label = np.where(npz_data['y_test'] > 0)[1]

    else:
        raise NotImplementedError

    with open(os.path.join(arg.joint_dir, 'epoch1_test_score.pkl'), 'rb') as r1:
        r1 = list(pickle.load(r1).items())

    with open(os.path.join(arg.bone_dir, 'epoch1_test_score.pkl'), 'rb') as r2:
        r2 = list(pickle.load(r2).items())

    if arg.joint_motion_dir is not None:
        with open(os.path.join(arg.joint_motion_dir, 'epoch1_test_score.pkl'), 'rb') as r3:
            r3 = list(pickle.load(r3).items())
    if arg.bone_motion_dir is not None:
        with open(os.path.join(arg.bone_motion_dir, 'epoch1_test_score.pkl'), 'rb') as r4:
            r4 = list(pickle.load(r4).items())

    if arg.joint_k2_dir is not None:
        with open(os.path.join(arg.joint_k2_dir, 'epoch1_test_score.pkl'), 'rb') as r5:
            r5 = list(pickle.load(r5).items())
    if arg.joint_motion_k2_dir is not None:
        with open(os.path.join(arg.joint_motion_k2_dir, 'epoch1_test_score.pkl'), 'rb') as r6:
            r6 = list(pickle.load(r6).items())
            
    if arg.joint_motion_dir is not None and arg.bone_motion_dir is not None:
        space = [(0.2, 1.2) for i in range(6)]
        result = gp_minimize(objective, space, n_calls=200, random_state=0)
        print('Maximum accuracy: {:.4f}%'.format(-result.fun * 100))
        print('Optimal weights: {}'.format(result.x))



