import ruamel.yaml

with open('vars_files/vcenter_info_vars.yml') as f:
    yaml = ruamel.yaml.YAML()  # defaults to round-trip if no parameters given
    vcenter_info = yaml.load(f)

with open('vars_files/deploy_nsx_tn_vars1.yml') as f:
    yaml = ruamel.yaml.YAML()  # defaults to round-trip if no parameters given
    code = yaml.load(f)

code['transport_nodes'][0]['node_deployment_info']['deployment_config'] = vcenter_info['edge1_deployment_config']
code['transport_nodes'][1]['node_deployment_info']['deployment_config'] = vcenter_info['edge2_deployment_config']

with open('vars_files/deploy_nsx_tn_vars1.yml', 'w') as f:
    yaml.default_flow_style=False
    yaml.dump(code, f)

with open('vars_files/deploy_nsx_tn_vars2.yml') as f:
    yaml = ruamel.yaml.YAML()  # defaults to round-trip if no parameters given
    code = yaml.load(f)

code['transport_nodes'][0]['node_deployment_info']['deployment_config'] = vcenter_info['edge1_deployment_config']
code['transport_nodes'][1]['node_deployment_info']['deployment_config'] = vcenter_info['edge2_deployment_config']

with open('vars_files/deploy_nsx_tn_vars2.yml', 'w') as f:
    yaml.default_flow_style=False
    yaml.dump(code, f)

with open('vars_files/deploy_nsx_tn_vars3.yml') as f:
    yaml = ruamel.yaml.YAML()  # defaults to round-trip if no parameters given
    code = yaml.load(f)

code['transport_nodes'][0]['node_deployment_info']['deployment_config'] = vcenter_info['edge1_deployment_config']
code['transport_nodes'][1]['node_deployment_info']['deployment_config'] = vcenter_info['edge2_deployment_config']

with open('vars_files/deploy_nsx_tn_vars3.yml', 'w') as f:
    yaml.default_flow_style=False
    yaml.dump(code, f)
