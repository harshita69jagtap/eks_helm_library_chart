# Steps to depoy cadence : 

Run migrations by following migrations.md file

Then, to deploy run 

**helm install cadence -f values.yaml -f values.prod.yaml . --namespace < namespace >**

