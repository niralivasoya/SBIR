from .base_options import BaseOptions

class TrainOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialze(self)
        self.parser.add_argument('--learning_rate', type=float, default=0.0002, help='learning rate for training')
        self.parser.add_argument('--num_epoch', type=int,required=True, help='the number of epoch for training')
        self.parser.add_argument('--n_labels', type=int,required=True,  help='the number of classes')
        self.parser.add_argument('--n_attrs', type=int,required=True,  help='the number of attribute')
        self.parser.add_argument('--weight_decay', type=float , default=0.005, help='weight decay rate for regularization')

        self.parser.add_argument('--loss_type', type=str, default='triplet|cls|attr,three_loss', help='The loss for training')        
        self.parser.add_argument('--loss_rate', type=str, default='3.0,0.5,0', help='The loss rate for different loss')
        #self.parser.add_argument('--loss_type', type=str, default='triplet_loss', help='The loss for training')                
        self.parser.add_argument('--augment_types', type=str, default=',cvt_dlg,cvt_dl', help='The augment type of the sketch data')
        self.parser.add_argument('--sketchy_photo_types', type=str, default='tx_000000000000', help='sketchy photo type')
        self.parser.add_argument('--sketchy_sketch_types', type=str, default='tx_000000000000', help='sketchy sketch type')
        self.parser.add_argument('--save_latest_freq', type=int, default=5000, help='frequency of saving the latest results')
        self.parser.add_argument('--save_epoch_freq', type=int, default=5, help='frequency of saving checkpoints at the end of epochs')        
        self.parser.add_argument('--print_freq', type=int, default=100, help='frequency of showing training results on console')
        self.parser.add_argument('--continue_train', action='store_true', help='continue training: load the start epoch model')
        self.parser.add_argument('--trained_model', type=str,  help='Load which model to continue training')
        self.parser.add_argument('--start_epoch', type=int, default=0, help='Start epoch for continue training')
        #self.parser.add_argument('--margin', type=float, default=100, help='frequency of showing training results on console')
        #self.parser.add_argument('--pool_size', type=int, default=50, help='the size of image buffer that stores previously generated images')
        self.update()
        
    def parse_specific_args(self):
        BaseOptions.parse_specific_args(self)
        self.opt.loss_rate = (float(rate) for rate in self.opt.loss_rate.split(','))
        self.opt.augment_types = (augment_type for augment_type in self.opt.augment_types.split(','))
        self.opt.sketchy_photo_types = (photo_type for photo_type in self.opt.sketchy_photo_types.split(','))
        self.opt.sketchy_sketch_types = (sketch_type for sketch_type in self.opt.sketchy_sketch_types.split(','))
        self.opt.loss_type, self.opt.loss_flag = self.opt.loss_type.split(',')
        self.opt.loss_type = self.opt.loss_type.split('|')
        self.opt.is_train = True

