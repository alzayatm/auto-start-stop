import boto3

ec2 = boto3.resource('ec2')
def start_servers(event, context):
    filters = [{ 'Name': 'tag:autoStart', 'Values': ['True']}]
    ec2.instances.filter(Filters=filters).start()

def stop_servers(event, context):
     for instance in ec2.instances.all():
          if(instance.tags is None):
               instance.stop()
          else:
               not_tagged_properly = True
               for tag in instance.tags:
                    if ((tag['Key'] == 'autoOff' and tag['Value'] == 'True') or (tag['Key'] == 'autoOff' and tag['Value'] != 'False')):
                         instance.stop()

                    if(tag['Key'] == 'autoOff'):
                         not_tagged_properly = False
                 
               if (not_tagged_properly):
                    instance.stop()


