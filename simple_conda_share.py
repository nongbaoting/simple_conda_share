#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File            : simple_conda_share.py
# @Date            : 2020/09/08 10:00:05
# @Author          : Baoting Nong (523135753@qq.com)
# @Link            : https://github.com/nongbaoting
# @Version         : 1.0.0
# @Description     : 

import os, re, fire, json


class Conda_Share:

    def __init__(self, env_name):
        self.env_name = env_name
    
    def get_full_dependencies(self, ):
        tmp_simle = f"simple_conda_share.{self.env_name}.json"
        os.system(f"conda env export --name {self.env_name} --json >{tmp_simle}")
        with open(f'{tmp_simle}') as f:
             dat = json.load(f)
             #print(dat)
        os.system(f'rm {tmp_simle}')

        self.full = dat

    def get_conda_installs(self):
        tmp_simle =  f'simple_conda_share.conda_install.{self.env_name}.json'
        os.system(f'conda env export --name {self.env_name} --json --from-history > {tmp_simle}' )
        with open(f'{tmp_simle}') as f:
             dsim = json.load(f)
             #print(dsim)
        os.system(f'rm {tmp_simle}')

        self.simple = dsim

    def output_simple_version(self, ):
        new_dependecy=[]
        for pk_f in self.full['dependencies']:
            if isinstance(pk_f, str):
                pk_f_arr = pk_f.split('=')
                pk_f_s = f'{pk_f_arr[0]}={pk_f_arr[1]}'

                if re.match('pip', pk_f):
                    new_dependecy.append(pk_f_s)

                for pk_s  in self.simple['dependencies']:
                    pk_s_ = pk_s.split("=")[0]
                    if pk_s_ == pk_f_arr[0] :
                        new_dependecy.append(pk_f_s)
                        # print(pk_f_s)
            elif isinstance(pk_f, dict):
                new_dependecy.append(pk_f)

        new_dat = self.full.copy()
        new_dat['dependencies'] = new_dependecy
        new_dat['channels'] =''
        if "prefix" in new_dat:
            del new_dat['prefix']

        with open(f'{self.env_name}.simple.yml', 'w') as fo:
            fo.write('name: ' + self.env_name + '\n' )
            fo.write("channels:\n")
            fo.write('dependencies:\n')
            for pk in new_dat['dependencies']:
                if isinstance(pk, str):
                    fo.write('  - ' + pk + '\n')
                elif isinstance(pk,dict):
                    fo.write('  - ' + 'pip:' + '\n')
                    for pk_pip in pk['pip']:
                        fo.write('    - ' + pk_pip + '\n')
                        

            print('complete !\nyout can create new environment with command:\n')
            print(f'conda env create -n {self.env_name} -f {self.env_name}.simple_conda_share.yml\n')

def main(env_name):
    conda_share = Conda_Share(env_name)
    conda_share.get_full_dependencies()
    conda_share.get_conda_installs()
    conda_share.output_simple_version()
if __name__ == '__main__':
    fire.Fire(main)