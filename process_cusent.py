import re
fid = open("/home/gyzhang/projects/tacotron2/datasets/cusent-female-filelists/cusent_audio_text_train_filelist.txt", 'r')
all_lines = fid.readlines()
fid.close()
with open('train_files.txt', 'w') as tfid:
    for one_line in all_lines:
        wav_file_path = re.split('\|', one_line.strip())[1]
        tfid.write(wav_file_path + '\n')