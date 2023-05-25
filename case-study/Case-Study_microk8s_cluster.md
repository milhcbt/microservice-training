setup master kubernates
```sh
~$ microk8s config
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUREekNDQWZlZ0F3SUJBZ0lVQm5pQWdhNkRCbjVPNUNVbnVPQnhhU3lpM0drd0RRWUpLb1pJaHZjTkFRRUwKQlFBd0Z6RVZNQk1HQTFVRUF3d01NVEF1TVRVeUxqRTRNeTR4TUI0WERUSXpNRFV5TkRFNU1UWTBNVm9YRFRNegpNRFV5TVRFNU1UWTBNVm93RnpFVk1CTUdBMVVFQXd3TU1UQXVNVFV5TGpFNE15NHhNSUlCSWpBTkJna3Foa2lHCjl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUEyS0VSaFNtYlQwQjNMTHRrOTVHeklHRHg2NktvK054Z3M0djEKR0JjWlBvUHJSY3laOWdHbEgwbGxLZG84NVFibE05OTFYNm1LaHZCQnRaZ1ZwMkdJcGdWNEpKMWgxeCsxL3cxcwphUGdEalJ5Nm1RaU5HYmlaZ2FXaXRCdHp3c3N0T0lEODYzRS9wMWJBUHEzUS9zS3NkMnlyU3JrT0tYT3FaVmdQCkxZSFUza1ZySjdnSDJmQUlNOWIycU9ibjVqYlN4d3VoTVRZRXdHUGFtbjBWZ1hadk1rTStraS9nR1psK3l1V2QKcFJxMVFISFp1WUFYZ1RueWQ4dU9MQXNQT01xTXJtMkFsTVIvVWEvMXB5R01oblY3aTA2ODhwaTA3YXZsWjRNYQpLWXJLZ05VRzA2amJmc2pxZFFnUVhmVkRSbTRnTFhvRDZLMHlqdlVsak55bm9OdFNoUUlEQVFBQm8xTXdVVEFkCkJnTlZIUTRFRmdRVUcrSU13aVdHMjh6Y2hsQUI5ODNyUzloMmlTa3dId1lEVlIwakJCZ3dGb0FVRytJTXdpV0cKMjh6Y2hsQUI5ODNyUzloMmlTa3dEd1lEVlIwVEFRSC9CQVV3QXdFQi96QU5CZ2txaGtpRzl3MEJBUXNGQUFPQwpBUUVBajRuMUVIZVR3dk90aEpTUHE0REVjWUFmR2JNWVMva3FTK2p4Q1FBL0pCNGZOWHVuSHZtL3VDMm5JNkM0ClNSYXR4VC9lMWVMcUJFcnl2eG1qUnVzZU53SnpIL2ZKVFRXaUxFaXk5YlRFNmdLUjlTTnlodFlPN0hHSmNXbXgKM1YzVlY3dmwwSHBib3pRWHA0QlBGMWV2TklFc251OXN4UjFTTjg1QmVvZzFhYjF0aXN2RmIrZWducXk5QXkregplb0kzZmJFdGJvY0FBOUtKT3RmY2k4ZERhZm9GT0ZXRTdZbmhGb2x0L3d4Y0dSZWVLY0VYQjhnZXQvUFk0Z3cxCi9pempXSUt5c3Y1azZXUlVyVHhueGlzNE5OYWtkeUI5T2wydVVtQ1QrRlMwS2hoMDZLT3cvRXZiM3BSamVzYVAKMmtEdmNHb0lUSGN5VGcvN2EvN2ZuVEVPMGc9PQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
    server: https://192.168.137.2:16443
  name: microk8s-cluster
contexts:
- context:
    cluster: microk8s-cluster
    user: admin
  name: microk8s
current-context: microk8s
kind: Config
preferences: {}
users:
- name: admin
  user:
    token: d2czd2hCQXZPLzFaMUdyRUozaXhmVUptK3VtckZnQ0Y2MW5KdmZHMUhrZz0K
```
add-node
```sh
$ microk8s add-node
From the node you wish to join to this cluster, run the following:
microk8s join 192.168.137.2:25000/9912aa07935c27b43ec0c6e022424f18/25d8a80b9f28

Use the '--worker' flag to join a node as a worker not running the control plane, eg:
microk8s join 192.168.137.2:25000/9912aa07935c27b43ec0c6e022424f18/25d8a80b9f28 --worker

If the node you are adding is not reachable through the default interface you can use one of the following:
microk8s join 192.168.137.2:25000/9912aa07935c27b43ec0c6e022424f18/25d8a80b9f28
```

Run microk8s config > ~/.kube/microk8s-config to save the kubeconfig file in your home directory.
Run export KUBECONFIG=~/.kube/microk8s-config to set the KUBECONFIG environment variable to your kubeconfig file.
Run k9s to launch k9s with the microk8s context.

I can help you with some general steps to setup a microk8s cluster on Ubuntu, but you may need to adjust them according to your specific hardware and network configuration. Here are the steps:

1. Install microk8s on each of the three orange pi devices using snap²⁴⁵:
```
sudo snap install microk8s --classic
```
2. Add your ubuntu user to the microk8s group on each device²⁵:
```
sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
```
3. Re-enter the session for the group update to take place on each device²:
```
su - $USER
```
4. Check the status of microk8s on each device and wait for it to be ready²:
```
microk8s status --wait-ready
```
5. On one of the devices (let's say pione), run the `microk8s add-node` command to get the joining instructions for the cluster³:
```
microk8s add-node
```
6. On the other two devices (pitwo and pitree), run the `microk8s join` command with the instructions from step 5³. For example:
```
microk8s join 192.168.137.2:25000/92b2db237428470dc4fcfc4ebbd9dc81/2c0cb3284b05
```
7. On pione, check the nodes in the cluster using `microk8s kubectl get nodes`³. You should see something like this:
```
NAME      STATUS   ROLES    AGE   VERSION
pione     Ready    <none>   10m   v1.27.0
pitwo     Ready    <none>   5m    v1.27.0
pitree    Ready    <none>   3m    v1.27.0
```
8. Optionally, enable some add-ons for your cluster, such as dns and hostpath-storage²:
```
microk8s enable dns hostpath-storage
```

That's it! You have successfully set up a microk8s cluster on three orange pi devices running Ubuntu.

Source: Conversation with Bing, 5/25/2023
(1) MicroK8s - Get started. https://microk8s.io/docs/getting-started.
(2) Install and Use MicroK8s on Ubuntu - Linux Tutorials - Learn Linux .... https://linuxconfig.org/install-and-use-microk8s-on-ubuntu.
(3) How to Install MicroK8s on Ubuntu - storagetutorials.com. https://www.storagetutorials.com/how-to-install-microk8s-on-ubuntu/.
(4) MicroK8s - Create a MicroK8s cluster. https://microk8s.io/docs/clustering.
(5) How to Install MicroK8s on Ubuntu - storagetutorials.com. https://bing.com/search?q=how+to+setup+microk8s+cluster+on+ubuntu.
(6) MicroK8s on Ubuntu : A Getting Started Guide - ATA Learning. https://adamtheautomator.com/microk8s/.