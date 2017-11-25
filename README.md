# 2017 Computational Vision Project

## Team members:
### Fengyang Zhang, Jianfeng Chi, Yutong Wang, Rongjia Gao, Wei Qian


#### Fengyang: WGAN without L1 distance
python pix2pix_wgan.py \
   --mode train \
   --output_dir maps_trained/ \
   --max_epochs 100 \
   --input_dir train/ \
   --which_direction AtoB \
   --l1_weight 0
   
#### xxx: WGAN with L1 distance
python pix2pix_wgan.py \
   --mode train \
   --output_dir maps_trained/ \
   --max_epochs 100 \
   --input_dir train/ \
   --which_direction AtoB \
   --l1_weight 1
   
#### xxx: Original GAN
python pix2pix.py \
   --mode train \
   --output_dir maps_trained_1/ \
   --max_epochs 100 \
   --input_dir train/ \
   --which_direction AtoB \
   --checkpoint maps_trained_1
