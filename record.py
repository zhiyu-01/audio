import wave

import pyaudio


def audio_record(file_name, rec_time):
        chunk = 1024
        formate = pyaudio.paInt16   #16bit编码格式（2个字节）
        channels = 2    #单声道
        rate = 16000  #采样率
 
        p = pyaudio.PyAudio()
 
        stream = p.open(format = formate,
                        channels= channels,
                        rate =rate,
                        input= True,
                        input_device_index=2,
                        frames_per_buffer=chunk)
        
        q=pyaudio.PyAudio()
        stream1=q.open(format=formate,channels=channels,rate=rate,output=True)
 
 
        print("开始录制")
 
        #录制的音频数据
        frames = []
 
        for i in range(0, int(rate / chunk * rec_time)):
            data = stream.read(chunk)
            frames.append(data)
            # stream1.write(data)
 
        #录制完成
        stream.stop_stream()
        stream.close()
        p.terminate()
 
        print("完成录制")
 
        # wave是录音时用的标准的WINDOWS文件格式，文件的扩展名为WAV
        # 保存录音
        file = wave.open(file_name, "wb")
        file.setnchannels(channels)
        file.setsampwidth(p.get_sample_size(formate))   #或者sampwidth=2(2个字节16位);  file.setsampwidth(sampwidth)
        file.setframerate(rate)  #帧速率
        file.writeframes(b''.join(frames))   #把数据加进去，存到硬盘中
        file.close()

def play():
    chunk=1024  #2014kb
    wf=wave.open(r"test.wav",'rb')
    p=pyaudio.PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
 
    data = wf.readframes(chunk)  # 读取数据
    print(data)
    while data != b'':  # 播放  
        stream.write(data)
        data = wf.readframes(chunk)
        print('while循环中！')
        # print(data)
    stream.stop_stream()   # 停止数据流
    stream.close()
    p.terminate()  # 关闭 PyAudio
    print('play函数结束！')

audio_record("test.wav", 5)
play()
