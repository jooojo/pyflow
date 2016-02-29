"""
    tools for collecting data in flowsets.
"""
import os

from sklearn.cross_validation import train_test_split

class FlowDataset(object):
    def __init__(self):
        self.frame_list = []
        self.train_list = []
        self.test_list = []

    def shuffle(self):
        self.train_list, self.test_list = train_test_split(self.frame_list)


class MPISintel(FlowDataset):
    def __init__(self, path):
        FlowDataset.__init__(self)
        self.collect_sintel_files(path)
        self.shuffle()

    def _get_triple(self, flow_file):
        ext = 'png'
        fprev_file = flow_file.replace('flow','final').replace('flo', ext)
	under_pos = fprev_file.rfind('_')
	dot_pos = fprev_file.rfind('.')
	pre = fprev_file[:under_pos]
	idx = str(int(fprev_file[under_pos+1:dot_pos])+1).zfill(4)
        fnext_file= '.'.join(('_'.join((pre, idx)), ext))
        return (flow_file, fprev_file, fnext_file)

    def collect_sintel_files(self, path):
        for parent, dirs, files in os.walk(path):
            self.frame_list += [self._get_triple(os.path.join(parent, file)) for file in files[1:]]
