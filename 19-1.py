#!/usr/bin/env python3

import re

workflows = {}
parts = None

variable_names = ['x', 'm', 'a', 's']

with open('in.19', 'r') as fd:
    for line in fd:
        if len(line) > 1:
            if parts == None:
                m = re.fullmatch(r'(\w+){(.*)}\n', line)
                name, rules = m.group(1,2)
                rules = re.split(r',', rules)
                for i, rule in enumerate(rules):
                    if ':' in rule:
                        expr, dest = rule.split(':')
                        if '<' in expr:
                            op = '<'
                            var, num = expr.split('<')
                            var = variable_names.index(var)
                        elif '>' in expr:
                            op = '>'
                            var, num = expr.split('>')
                            var = variable_names.index(var)
                        else:
                            raise RuntimeError(f'Unknown comparison operator: {expr[2]}')
                        rules[i] = [var, op, int(num), dest]

                workflows[name] = rules
                # print(f'name: {name}, rules: {rules}')
            else:
                m = re.fullmatch(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}\n', line)
                x, m, a, s = m.group(1, 2, 3, 4)
                parts.append([int(x), int(m), int(a), int(s)])
        else:
            #print()
            parts = []

def next_step(part: [int], workflow: str, workflows: {}) -> str:
    for wf in workflows[workflow]:
        if isinstance(wf, str):
            return wf
        elif isinstance(wf, list):
            if wf[1] == '<' and part[wf[0]] < wf[2]:
                return wf[3]
            elif wf[1] == '>' and part[wf[0]] > wf[2]:
                return wf[3]
    raise RuntimeError('Unexpected next_step is unknown')

# Run rules until part gets accepted or rejected
# Start with workflow in.
accepted = []

for part in parts:
    x, m, a, s = part
    workflow = 'in'
    while workflow not in 'AR':
        workflow = next_step(part, workflow, workflows)
    if workflow == 'A':
        accepted.append(part)

result = 0
for part in accepted:
    result += sum(part)

print(result)
