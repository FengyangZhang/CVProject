# 2017 Computational Vision Project

## Team members:
### Fengyang Zhang, Jianfeng Chi, Yutong Wang, Rongjia Gao, Wei Qian


#### WGAN without L1 distance
nohup python pix2pix_wgan.py --mode train --output_dir maps_trained/ --max_epochs 100 --input_dir train/ --which_direction AtoB --l1_weight 0 --checkpoint maps_trained_3 > out.txt
   
#### WGAN with L1 distance
nohup python pix2pix_wgan.py --mode train --output_dir maps_trained/ --max_epochs 200  --input_dir train/ --which_direction AtoB --l1_weight 5 > out.txt
   
#### Original GAN
nohup python pix2pix.py --mode train --output_dir maps_trained_1/ --max_epochs 100 --input_dir train/ --which_direction AtoB --checkpoint maps_trained_1 > out.txt
