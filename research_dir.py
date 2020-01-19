# python3
# this is for create research directory
# idea comes from James Scott Long - The Workflow of Data Analysis Using Stata-Stata Press (2009)
import os,sys

class research_dir():
    def __init__(self,proj_name,path=None):
        self.proj_name = proj_name
        if path:
            self.proj_path = path
        else:
            self.proj_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname('README.md')),'..')),proj_name)
        
        self.path_name_book = self.create_path_name_book()
        
        if not os.path.exists(self.proj_path):
            os.mkdir(self.proj_path)
        print('project path: {}'.format(self.proj_path))
            
    def create_path_name_book(self):
        '''
        create name book level by level
        '''
        path_name_dir = {}
        # diretory level 1
        path_name_dir['to_file'] = {'purpose': 'file to examine and move to appropriate location',
                                              'subpath':{}}
        path_name_dir['administration'] = {'purpose': 'Administration',
                                              'subpath':{}}
        path_name_dir['documentation'] = {'purpose': 'documentation for project',
                                              'subpath':{}}
        path_name_dir['hold_then_delete'] = {'purpose': 'delete when project is complete',
                                              'subpath':{}}
        path_name_dir['posted'] = {'purpose': 'completed files that cannot be changed',
                                              'subpath':{}}
        path_name_dir['readings'] = {'purpose': 'file to examine and move to appropriate location',
                                              'subpath':{}}
        path_name_dir['work'] = {'purpose': 'work directory',
                                              'subpath':{}}
        # directory level 2
        # administration
        path_name_dir['administration']['subpath'].update({
            'proposal': {
            'purpose':'grant proposal and related materials'}
        })
        # documentation
        path_name_dir['documentation']['subpath'].update({
            'codebooks': {
            'purpose':'codebooks for source and constructed variables'}
        })
        path_name_dir['documentation']['subpath'].update({
            'data_clean_log': {
            'purpose':'log for data clean'}
        })
        path_name_dir['documentation']['subpath'].update({
            'data_analysis_log': {
            'purpose':'log for data clean'}
        })
        # posted
        path_name_dir['posted']['subpath'].update({
            'datasets': {
            'purpose':'datasets',
            'subpath':{
                'deried':{'purpose':'dataset constructed from original data'},
                'source':{'original data without modifications'}
            }}
        })
        path_name_dir['posted']['subpath'].update({
            'text': {
            'purpose':'completed drafts of paper'}
        })
        path_name_dir['posted']['subpath'].update({
            'operation': {
            'purpose':'code and log to git',
            'subpath':{
                'data_clean': {'purpose':'clean data and variable construction'},
                'data_describ': {'purpose':'descriptive statistics and sample selection'},
                'panelmodels': {
                    'purpose':'panel models for discriminations',
                    'subpath':{
                        'model1':{'purpose':'codes and logs used in analysis'}
                    }}
            }}})
        path_name_dir['posted']['subpath'].update({
            'fig_tables': {'purpose':'results graph and table of data'}
        })
        # work
        path_name_dir['work']['subpath'].update({
            'to_do': {
            'purpose':'work that hasn\'t been started'}
        })
        path_name_dir['work']['subpath'].update({
            'datasets': {
            'purpose':'datasets',
            'subpath':{
                'deried':{'purpose':'dataset constructed from original data'},
                'source':{'original data without modifications'}
            }}
        })
        path_name_dir['work']['subpath'].update({
            'text': {
            'purpose':'completed drafts of paper'}
        })
        path_name_dir['work']['subpath'].update({
            'operation': {
            'purpose':'code and log to git',
            'subpath':{
                'data_clean': {'purpose':'clean data and variable construction'},
                'data_describ': {'purpose':'descriptive statistics and sample selection'},
                'panelmodels': {
                    'purpose':'panel models for discriminations',
                    'subpath':{
                        'model1':{'purpose':'codes and logs used in analysis'}
                    }}
            }}})
        path_name_dir['work']['subpath'].update({
            'fig_tables': {
            'purpose':'results: graph and table of data'}
        })
        
        return path_name_dir
    
    def create_path(self, new_name_book=False):
        '''
        create dir base on path name book
        ::param path_name_book default created by created_path_name_book
        '''
        if new_name_book:
            path_name_book = new_name_book
        else:
            path_name_book = self.path_name_book
        for path_l1,v1 in path_name_book.items():
            if not os.path.exists(os.path.join(self.proj_path,path_l1)):
                os.mkdir(os.path.join(self.proj_path,path_l1))
            self.create_subpath(path_dict=v1, parent_path_l0=os.path.join(self.proj_path,path_l1))
        self.show_dir(self.proj_path)
        
    def create_subpath(self, path_dict, parent_path_l0):
        '''
        sub function used in create path
        ::param path_dict a dictionary with key "subpath"
        ::param parent_path_l0 the parent path of the subpath
        '''
        try:
            if path_dict.get('subpath'):
                for path_l1,v1 in path_dict['subpath'].items():
                    parent_path_l1 = os.path.join(parent_path_l0,path_l1)
                    if not os.path.exists(parent_path_l1):
                        os.mkdir(parent_path_l1)
                    self.create_subpath(path_dict=v1, parent_path_l0=parent_path_l1)
        except:
            pass
        
    def show_dir(self, path, depth=0):
        '''
        print a tree of directory
        ::param path
        ::param depth default 0
        '''
        if depth:
            sep = '|   '*(depth-1)+'|---'
        else:
            sep = ''
        print(sep+os.path.split(path)[-1])
        if os.path.isdir(path):
            for subpath in os.listdir(path):
                subpath_full = os.path.join(path,subpath)
                subdepth = depth+1
                self.show_dir(subpath_full,subdepth)
        
    
if __name__ == "__main__":
    confirm_proj_name = 'n'
    while confirm_proj_name == 'n':
        proj_name = input('enter project name:')
        confirm_proj_name = input('confim? if not press \'n\' and \'enter\'')
    research = research_dir(proj_name)
    research.create_path()
    print('project dir created')
    input()
