import argparse
parser = argparse.ArgumentParser(description="PyTorch implementation of Temporal Segment Networks")
parser.add_argument('dataset', type=str, choices=['ucf101', 'hmdb51', 'kinetics', 'twentyBN'])
parser.add_argument('modality', type=str, choices=['RGB', 'Flow', 'RGBDiff'])
parser.add_argument('train_list', type=str)
parser.add_argument('val_list', type=str)
parser.add_argument('--model', type=str, default='TSN', choices=['TSN', 'TSM', 'GSM', 'etc'])


# ========================= Model Configs ==========================
parser.add_argument('--arch', type=str, default="resnet50")
parser.add_argument('--mixer1', type=str, default=None)
parser.add_argument('--mixer2', type=str, default=None)
parser.add_argument('--concat_shift', type=str, default=None)
parser.add_argument('--num_segments', type=int, default=8)
parser.add_argument('--consensus_type', type=str, default='avg',
                    choices=['avg', 'max', 'topk', 'identity', 'rnn', 'cnn'])
parser.add_argument('--k', type=int, default=3)

parser.add_argument('--dropout', '--do', default=0, type=float,
                    metavar='DO', help='dropout ratio (default: 0)')
parser.add_argument('--loss_type', type=str, default="nll",
                    choices=['nll'])

# ========================= Learning Configs ==========================
parser.add_argument('--epochs', default=45, type=int, metavar='N',
                    help='number of total epochs to run')
parser.add_argument('-b', '--batch-size', default=64, type=int,
                    metavar='N', help='mini-batch size (default: 64)')
parser.add_argument('--lr', '--learning-rate', default=0.01, type=float,
                    metavar='LR', help='initial learning rate')
parser.add_argument('--lr_steps', default=[15, 30], type=float, nargs="+",
                    metavar='LRSteps', help='epochs to decay learning rate by 10')
parser.add_argument('--momentum', default=0.9, type=float, metavar='M',
                    help='momentum')
parser.add_argument('--weight-decay', '--wd', default=5e-4, type=float,
                    metavar='W', help='weight decay (default: 5e-4)')
parser.add_argument('--clip-gradient', '--gd', default=None, type=float,
                    metavar='W', help='gradient norm clipping (default: disabled)')
parser.add_argument('--no_partialbn', '--npb', default=False, action="store_true")

# ========================= Monitor Configs ==========================
parser.add_argument('--print-freq', '-p', default=300, type=int,
                    metavar='N', help='print frequency (default: 300)')
parser.add_argument('--valid-freq', default=100, type=int,
                    metavar='N', help='validation print frequency (default: 100)')
parser.add_argument('--eval-freq', '-ef', default=5, type=int,
                    metavar='N', help='evaluation frequency (default: 5)')


# ========================= Runtime Configs ==========================
parser.add_argument('-j', '--workers', default=100, type=int, metavar='N',
                    help='number of data loading workers (default: 100)')
parser.add_argument('--resume', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',
                    help='evaluate model on validation set')
parser.add_argument('--snapshot_pref', type=str, default="")
parser.add_argument('--start-epoch', default=0, type=int, metavar='N',
                    help='manual epoch number (useful on restarts)')
parser.add_argument('--gpus', nargs='+', type=int, default=None)
parser.add_argument('--flow_prefix', default="", type=str)








