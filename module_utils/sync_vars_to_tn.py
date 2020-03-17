import ruamel.yaml

with open('vars_files/vcenter_info_vars.yml') as f:
    yaml = ruamel.yaml.YAML()  # defaults to round-trip if no parameters given
    vcenter_info = yaml.load(f)

with open('vars_files/deploy_nsx_tn_vars1.yml') as f:
    yaml = ruamel.yaml.YAML()  # defaults to round-trip if no parameters given
    code = yaml.load(f)

code['transport_nodes'][0]['display_name'] = vcenter_info['edge1_display_name']
code['transport_nodes'][1]['display_name'] = vcenter_info['edge2_display_name']
code['transport_nodes'][0]['node_deployment_info'] = vcenter_info['node1_node_deployment_info']
code['transport_nodes'][1]['node_deployment_info'] = vcenter_info['node2_node_deployment_info']
code['edge_clusters'] = vcenter_info['edge_clusters']

with open('vars_files/deploy_nsx_tn_vars1.yml', 'w') as f:
    yaml.default_flow_style=False
    yaml.dump(code, f)

with open('vars_files/deploy_nsx_tn_vars2.yml') as f:
    yaml = ruamel.yaml.YAML()  # defaults to round-trip if no parameters given
    code = yaml.load(f)

code['transport_nodes'][0]['display_name'] = vcenter_info['edge1_display_name']
code['transport_nodes'][1]['display_name'] = vcenter_info['edge2_display_name']
code['transport_nodes'][0]['node_deployment_info'] = vcenter_info['node1_node_deployment_info']
code['transport_nodes'][1]['node_deployment_info'] = vcenter_info['node2_node_deployment_info']
code['edge_clusters'] = vcenter_info['edge_clusters']


with open('vars_files/deploy_nsx_tn_vars2.yml', 'w') as f:
    yaml.default_flow_style=False
    yaml.dump(code, f)

with open('vars_files/deploy_nsx_tn_vars3.yml') as f:
    yaml = ruamel.yaml.YAML()  # defaults to round-trip if no parameters given
    code = yaml.load(f)

code['transport_nodes'][0]['display_name'] = vcenter_info['edge1_display_name']
code['transport_nodes'][1]['display_name'] = vcenter_info['edge2_display_name']
code['transport_nodes'][0]['node_deployment_info'] = vcenter_info['node1_node_deployment_info']
code['transport_nodes'][1]['node_deployment_info'] = vcenter_info['node2_node_deployment_info']
code['edge_clusters'] = vcenter_info['edge_clusters']


with open('vars_files/deploy_nsx_tn_vars3.yml', 'w') as f:
    yaml.default_flow_style=False
    yaml.dump(code, f)
