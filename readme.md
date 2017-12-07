devops exercise for brealtime

#to launch instance using cloudformation
aws cloudformation create-stack --stack-name brealtime \
--template-body file://ec2-setup.yaml
