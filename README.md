# lj-format-japanese-g2p
Takes a LJ-Speech format TalkNet test/validation file in Japanese/Kanji and uses pyopenjtalk's g2p to format it correctly for training Japanese voices in neuTalk.

```
python ntk_kanji2phonemes.py
```
If you want the script to convert to TalQu phones, type 'y' or 'yes' at the end of the script like this
```
python ntk_kanji2phonemes.py yes
```
