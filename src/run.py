import sys, os
import argparse
import numpy as np

try:
    from maskmaker import MaskMaker
except:
    print('Searching subdirectory `/src/` for maskmaker.py')
    sys.path.append('src')

def main(args):
    mm = MaskMaker(
        nRegions=args.regions,
        xyTranslations=args.shifts,
        polyEdges=args.edges,
        imageSize=args.dimensions,
        randSeed=args.seed,
        rescaler=args.rescaler
    )

    mm.saveMask(file_name=args.saveAs)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='MaskMaker')

    parser.add_argument('--regions', type=int, default=15,
                         help='Number of regions')
    random_positions = [(np.random.randint(256), np.random.randint(256))
                        for i in range(20)]
    parser.add_argument('--shifts', type=list, default=random_positions,
                        help='List of translations in (x,y) direction.')
    random_edges = [np.random.randint(3,8) for i in range(20)]
    parser.add_argument('--edges', type=list, default=random_edges,
                        help='List of edges in the polygon')
    parser.add_argument('--dimensions', type=tuple, default=(256,256))
    parser.add_argument('--seed', type=int, default=420)
    parser.add_argument('--rescaler', type=int, default=21)
    parser.add_argument('--saveAs', type=str, default='mask.png')
    args1 = parser.parse_args()
    main(args1)

    
    
