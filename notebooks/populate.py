import ycpatch
# or just cp, and make this a notebook. make testing easier.

whichscan=1

if whichscan==1:
  path = '/mnt/lab/users/stelios/data/Jedi_exp/9_29_19/cellB_scan1/'
  ephys_filename = 'cellB2_0.h5'
  scan_filename = 'cellB_00001.tif'
elif whichscan==2:
  path = '/mnt/lab/users/stelios/data/Jedi_exp/10_4_19/cell1_scan1/'
  ephys_filename = 'cell1SP0_0.h5'
  scan_filename = 'cell1_00001.tif'

# formatting error here.
        scan = scanreader.read_scan(scan_filename)
        # Get attributes
        tuple_ = key.copy()  # in case key is reused somewhere else
        tuple_['nfields'] = scan.num_fields
        tuple_['nchannels'] = scan.num_channels
        tuple_['nframes'] = scan.num_frames
        tuple_['nframes_requested'] = scan.num_requested_frames
        tuple_['px_height'] = scan.image_height
        tuple_['px_width'] = scan.image_width
        tuple_['x'] = scan.motor_position_at_zero[0]
        tuple_['y'] = scan.motor_position_at_zero[1]
        tuple_['fps'] = scan.fps
        tuple_['zoom'] = Decimal(str(scan.zoom))
        tuple_['bidirectional'] = scan.is_bidirectional
        tuple_['usecs_per_line'] = scan.seconds_per_line * 1e6
        tuple_['fill_fraction'] = scan.temporal_fill_fraction
        tuple_['valid_depth'] = True
        # also need maunaully add some other values, like corr_ch etc.
        
tuple_['notes']=whichscan+datetime.datetime.today().strftime('%d-%m-%Y')
# make a new entry for notes keeping
tuple_['path']=path
# pipeline has somewhere to save the file path, off the top of my head



ycpatch.Scaninfo.insert1(tuple_)


ycpatch.Rastercorrection.populate()
ycpatch.Motioncorrection.populate()
