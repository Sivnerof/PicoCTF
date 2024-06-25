# Substitution2

## Description

It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher? Download the message [here](https://artifacts.picoctf.net/c/112/message.txt "PicoCTF link to download enciphered flag text file").

## Hints

* Try refining your frequency attack, maybe analyzing groups of letters would improve your results?

## Walkthrough

If we open the enciphered flag found in the [message.txt](./message.txt "Enciphered flag text file") file we'll find the following text.

```
nafyffoxenefufytpqnafymfppfentkpxeafbaxraezaqqpzqgswnfyefzwyxnhzqgsfnxnxqlexlzpwbxlrzhkfystnyxqntlbwezhkfyzatppflrfnafefzqgsfnxnxqlevqzwesyxgtyxphqlehenfgetbgxlxenytnxqlvwlbtgflntpemaxzatyfufyhwefvwptlbgtycfntkpfecxppeaqmfufymfkfpxfufnafsyqsfyswysqefqvtaxraezaqqpzqgswnfyefzwyxnhzqgsfnxnxqlxelqnqlphnqnftzautpwtkpfecxppekwntpeqnqrfnenwbflnexlnfyfenfbxltlbfozxnfbtkqwnzqgswnfyezxflzfbfvflexufzqgsfnxnxqletyfqvnflptkqyxqwetvvtxyetlbzqgfbqmlnqywllxlrzafzcpxenetlbfofzwnxlrzqlvxrezyxsneqvvflefqlnafqnafyatlbxeaftuxphvqzwefbqlfospqytnxqltlbxgsyquxetnxqltlbqvnflatefpfgflneqvspthmfkfpxfuftzqgsfnxnxqlnqwzaxlrqlnafqvvflexuffpfgflneqvzqgswnfyefzwyxnhxenafyfvqyftkfnnfyufaxzpfvqynfzafutlrfpxegnqenwbflnexltgfyxztlaxraezaqqpevwynafymfkfpxfufnatntlwlbfyentlbxlrqvqvvflexufnfzalxiwfexefeeflnxtpvqygqwlnxlrtlfvvfznxufbfvfleftlbnatnnafnqqpetlbzqlvxrwytnxqlvqzweflzqwlnfyfbxlbfvflexufzqgsfnxnxqlebqfelqnpftbenwbflnenqclqmnafxyflfghtefvvfznxufphtenftzaxlrnafgnqtznxufphnaxlcpxcftltnntzcfysxzqznvxetlqvvflexufphqyxflnfbaxraezaqqpzqgswnfyefzwyxnhzqgsfnxnxqlnatneffcenqrflfytnfxlnfyfenxlzqgswnfyezxflzftgqlraxraezaqqpfyenftzaxlrnafgflqwratkqwnzqgswnfyefzwyxnhnqsxiwfnafxyzwyxqexnhgqnxutnxlrnafgnqfospqyfqlnafxyqmltlbfltkpxlrnafgnqkfnnfybfvflbnafxygtzaxlfenafvptrxesxzqZNV{L6Y4G_4L41H515_15_73B10W5_8F1KV808}
```

This time we don't have a key, so we'll have to use [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis "Wikipedia page for frequency analysis"). There are many frequency analysis tools online; a good one can be found at [101 Computing](https://www.101computing.net/frequency-analysis/ "101 Computing frequency analysis tools").

Before we begin identifying which character maps to which, we start with a completely blank slate. Leaving our deciphered text looking like this, where every unknown character is represented with an asterisk.

```
****************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************{*6*4*_4*41*515_15_73*10*5_8*1**808}
```

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | ?        |
| B          | --><-- | ?        |
| C          | --><-- | ?        |
| D          | --><-- | ?        |
| E          | --><-- | ?        |
| F          | --><-- | ?        |
| G          | --><-- | ?        |
| H          | --><-- | ?        |
| I          | --><-- | ?        |
| J          | --><-- | ?        |
| K          | --><-- | ?        |
| L          | --><-- | ?        |
| M          | --><-- | ?        |
| N          | --><-- | ?        |
| O          | --><-- | ?        |
| P          | --><-- | ?        |
| Q          | --><-- | ?        |
| R          | --><-- | ?        |
| S          | --><-- | ?        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | ?        |
| W          | --><-- | ?        |
| X          | --><-- | ?        |
| Y          | --><-- | ?        |
| Z          | --><-- | ?        |

If we look at the ciphertext we can identify the flag, which will allow us to plug in our first values.

```sxzqZNV{L6Y4G_4L41H515_15_73B10W5_8F1KV808}```

We know the flag starts with ```picoCTF``` so we'll start mapping those to the characters ```sxzqZNV```.

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | ?        |
| B          | --><-- | ?        |
| C          | --><-- | ?        |
| D          | --><-- | ?        |
| E          | --><-- | ?        |
| F          | --><-- | ?        |
| G          | --><-- | ?        |
| H          | --><-- | ?        |
| I          | --><-- | ?        |
| J          | --><-- | ?        |
| K          | --><-- | ?        |
| L          | --><-- | ?        |
| M          | --><-- | ?        |
| N          | --><-- | T        |
| O          | --><-- | ?        |
| P          | --><-- | ?        |
| Q          | --><-- | O        |
| R          | --><-- | ?        |
| S          | --><-- | P        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | F        |
| W          | --><-- | ?        |
| X          | --><-- | I        |
| Y          | --><-- | ?        |
| Z          | --><-- | C        |

Deciphered text so far:

```
T******I*T*******OT*********T***I*****I***C*OO*CO*P*T****C**IT*CO*P*TITIO**I*C***I**C****P*T*IOT*****C****C********T****CO*P*TITIO**FOC**P*I***I**O****T******I*I*T**TIO*F*******T*****IC***********F**********T******I****O**********I***T**P*OP**P**PO**OF**I***C*OO*CO*P*T****C**IT*CO*P*TITIO*I**OTO***TOT**C***********I*****T***OTO**T*T****T*I*T****T**I******CIT****O*TCO*P*T***CI**C***F***I**CO*P*TITIO*****OFT*****O*IO***FF*I*****CO***O**TO****I**C**C**I*T*******C*TI**CO*FI**C*IPT*OFF****O*T**OT*******I*****I**FOC****O***P*O**TIO****I*P*O*I**TIO****OFT***********T*OFP********I****CO*P*TITIO*TO*C*I**O*T**OFF***I********T*OFCO*P*T****C**IT*I*T****FO*****TT*****IC**FO*T*C********I**TO*T****T*I*****IC***I***C*OO**F**T********I***T**T********T***I**OFOFF***I**T*C**I****I******TI**FO**O**TI*****FF*CTI****F*******T**TT**TOO*****CO*FI****TIO*FOC****CO**T****I***F***I**CO*P*TITIO***O***OT*****T****T*TO**O*T**I*********FF*CTI******T**C*I**T***TO*CTI****T*I***I*****TT*C***PICOCTFI***OFF***I****O*I**T***I***C*OO*CO*P*T****C**IT*CO*P*TITIO*T**T*****TO******T*I*T****TI*CO*P*T***CI**C***O***I***C*OO****T**C*I**T*****O*****O*TCO*P*T****C**IT*TOPI***T**I*C**IO*IT**OTI**TI**T***TO**P*O**O*T**I*O**********I**T***TO**TT****F***T**I***C*I***T**F***I*PICOCTF{*6*4*_4*41*515_15_73*10*5_8*1*F808}
```

Using frequency analysis we can see that the most common letter in the ciphertext is the letter "F" which shows up 175 times and takes up 13.6 percent of all characters used. We can replace this with the letter "E" which is the most common letter used in the English language and see how it fits but instead we'll do something better. If you look closely at the ciphertext there is a series of letters that repeat at a high frequency and that is ```CO*P*TITIO*```. This series of letters strongly resembles the word "COMPETITION". Assuming we're right, we can begin plugging in the new values.

* ```zqgsfnxnxql --> CO*P*TITIO*``` (Possibly "COMPETITION")

This would mean that the letter "g" maps to "M", "f" to "E", and "l" to "N".

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | ?        |
| B          | --><-- | ?        |
| C          | --><-- | ?        |
| D          | --><-- | ?        |
| E          | --><-- | ?        |
| F          | --><-- | E        |
| G          | --><-- | M        |
| H          | --><-- | ?        |
| I          | --><-- | ?        |
| J          | --><-- | ?        |
| K          | --><-- | ?        |
| L          | --><-- | N        |
| M          | --><-- | ?        |
| N          | --><-- | T        |
| O          | --><-- | ?        |
| P          | --><-- | ?        |
| Q          | --><-- | O        |
| R          | --><-- | ?        |
| S          | --><-- | P        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | F        |
| W          | --><-- | ?        |
| X          | --><-- | I        |
| Y          | --><-- | ?        |
| Z          | --><-- | C        |

Deciphered text so far:

```
T*E*EE*I*T*E*E***OT*E**E**E*T***I**E**I***C*OO*COMP*TE**EC**IT*COMPETITION*INC***IN*C**E*P*T*IOT*N***C**E*C****EN*ET*E*ECOMPETITION*FOC**P*IM**I**ON***TEM***MINI*T**TIONF*N**MENT*****IC***E*E****EF***N*M***ET***E**I****O*E*E**E*E*IE*ET*EP*OPE*P**PO*EOF**I***C*OO*COMP*TE**EC**IT*COMPETITIONI*NOTON**TOTE*C********E**I*****T***OTO*ET*T**ENT*INTE*E*TE*IN*N*E*CITE***O*TCOMP*TE**CIENCE*EFEN*I*ECOMPETITION***EOFTEN***O*IO***FF*I***N*COME*O*NTO**NNIN*C*EC**I*T**N*E*EC*TIN*CONFI**C*IPT*OFFEN*EONT*EOT*E***N*I**E**I**FOC**E*ONE*P*O**TION*N*IMP*O*I**TION*N*OFTEN***E*EMENT*OFP****E*E*IE*E*COMPETITIONTO*C*IN*ONT*EOFFEN*I*EE*EMENT*OFCOMP*TE**EC**IT*I*T*E*EFO*E**ETTE**E*IC*EFO*TEC*E**N*E*I*MTO*T**ENT*IN*ME*IC*N*I***C*OO**F**T*E**E*E*IE*ET**T*N*N*E**T*N*IN*OFOFFEN*I*ETEC*NI**E*I*E**ENTI**FO*MO*NTIN**NEFFECTI*E*EFEN*E*N*T**TT*ETOO***N*CONFI****TIONFOC**ENCO*NTE*E*IN*EFEN*I*ECOMPETITION**OE*NOT*E***T**ENT*TO*NO*T*EI*ENEM***EFFECTI*E****TE*C*IN*T*EMTO*CTI*E**T*IN**I*E*N*TT*C*E*PICOCTFI**NOFFEN*I*E**O*IENTE**I***C*OO*COMP*TE**EC**IT*COMPETITIONT**T*EE**TO*ENE**TEINTE*E*TINCOMP*TE**CIENCE*MON**I***C*OO*E**TE*C*IN*T*EMENO*****O*TCOMP*TE**EC**IT*TOPI**ET*EI*C**IO*IT*MOTI**TIN*T*EMTOE*P*O*EONT*EI*O*N*N*EN***IN*T*EMTO*ETTE**EFEN*T*EI*M*C*INE*T*EF***I*PICOCTF{N6*4M_4N41*515_15_73*10*5_8E1*F808}
```

The new mapping seems to fit, as a bunch of possible words start to jump out at us. One of these words being ```COMP*TE*``` which is most likely "COMPUTER".

* ```zqgswnfy --> COMP*TE*``` (Possibly "COMPUTER")

This would mean that "w" maps to "U" and "y" to "R".

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | ?        |
| B          | --><-- | ?        |
| C          | --><-- | ?        |
| D          | --><-- | ?        |
| E          | --><-- | ?        |
| F          | --><-- | E        |
| G          | --><-- | M        |
| H          | --><-- | ?        |
| I          | --><-- | ?        |
| J          | --><-- | ?        |
| K          | --><-- | ?        |
| L          | --><-- | N        |
| M          | --><-- | ?        |
| N          | --><-- | T        |
| O          | --><-- | ?        |
| P          | --><-- | ?        |
| Q          | --><-- | O        |
| R          | --><-- | ?        |
| S          | --><-- | P        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | F        |
| W          | --><-- | U        |
| X          | --><-- | I        |
| Y          | --><-- | R        |
| Z          | --><-- | C        |

Deciphered text so far:

```
T*EREE*I*T*E*ER**OT*ER*E**E*T***I**E**I***C*OO*COMPUTER*ECURIT*COMPETITION*INC*U*IN*C**ERP*TRIOT*N*U*C**ERC****EN*ET*E*ECOMPETITION*FOCU*PRIM*RI**ON***TEM***MINI*TR*TIONFUN**MENT*****IC**RE*ER*U*EFU**N*M*R*ET***E**I****O*E*ER*E*E*IE*ET*EPROPERPURPO*EOF**I***C*OO*COMPUTER*ECURIT*COMPETITIONI*NOTON**TOTE*C****U***E**I****UT***OTO*ET*TU*ENT*INTERE*TE*IN*N*E*CITE***OUTCOMPUTER*CIENCE*EFEN*I*ECOMPETITION**REOFTEN***ORIOU**FF*IR**N*COME*O*NTORUNNIN*C*EC**I*T**N*E*ECUTIN*CONFI**CRIPT*OFFEN*EONT*EOT*ER**N*I**E**I**FOCU*E*ONE*P*OR*TION*N*IMPRO*I**TION*N*OFTEN***E*EMENT*OFP****E*E*IE*E*COMPETITIONTOUC*IN*ONT*EOFFEN*I*EE*EMENT*OFCOMPUTER*ECURIT*I*T*EREFORE**ETTER*E*IC*EFORTEC*E**N*E*I*MTO*TU*ENT*IN*MERIC*N*I***C*OO**FURT*ER*E*E*IE*ET**T*NUN*ER*T*N*IN*OFOFFEN*I*ETEC*NI*UE*I*E**ENTI**FORMOUNTIN**NEFFECTI*E*EFEN*E*N*T**TT*ETOO***N*CONFI*UR*TIONFOCU*ENCOUNTERE*IN*EFEN*I*ECOMPETITION**OE*NOT*E***TU*ENT*TO*NO*T*EIRENEM***EFFECTI*E****TE*C*IN*T*EMTO*CTI*E**T*IN**I*E*N*TT*C*ERPICOCTFI**NOFFEN*I*E**ORIENTE**I***C*OO*COMPUTER*ECURIT*COMPETITIONT**T*EE**TO*ENER*TEINTERE*TINCOMPUTER*CIENCE*MON**I***C*OO*ER*TE*C*IN*T*EMENOU****OUTCOMPUTER*ECURIT*TOPI*UET*EIRCURIO*IT*MOTI**TIN*T*EMTOE*P*OREONT*EIRO*N*N*EN***IN*T*EMTO*ETTER*EFEN*T*EIRM*C*INE*T*EF***I*PICOCTF{N6R4M_4N41*515_15_73*10U5_8E1*F808}
```

Inbetween the words "COMPUTER" and "COMPETITION" we find the word ```*ECURIT*```, which is most likely "SECURITY".

```efzwyxnh --> *ECURIT*``` (Possibly "SECURITY")

New mappings: "e" to "S", "h" to "Y".

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | ?        |
| B          | --><-- | ?        |
| C          | --><-- | ?        |
| D          | --><-- | ?        |
| E          | --><-- | S        |
| F          | --><-- | E        |
| G          | --><-- | M        |
| H          | --><-- | Y        |
| I          | --><-- | ?        |
| J          | --><-- | ?        |
| K          | --><-- | ?        |
| L          | --><-- | N        |
| M          | --><-- | ?        |
| N          | --><-- | T        |
| O          | --><-- | ?        |
| P          | --><-- | ?        |
| Q          | --><-- | O        |
| R          | --><-- | ?        |
| S          | --><-- | P        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | F        |
| W          | --><-- | U        |
| X          | --><-- | I        |
| Y          | --><-- | R        |
| Z          | --><-- | C        |

Deciphered text so far:

```
T*EREE*ISTSE*ER**OT*ER*E**EST***IS*E**I**SC*OO*COMPUTERSECURITYCOMPETITIONSINC*U*IN*CY*ERP*TRIOT*N*USCY*ERC****EN*ET*ESECOMPETITIONSFOCUSPRIM*RI*YONSYSTEMS**MINISTR*TIONFUN**MENT**S**IC**RE*ERYUSEFU**N*M*R*ET***ES*I**S*O*E*ER*E*E*IE*ET*EPROPERPURPOSEOF**I**SC*OO*COMPUTERSECURITYCOMPETITIONISNOTON*YTOTE*C****U***ES*I**S*UT**SOTO*ETSTU*ENTSINTERESTE*IN*N*E*CITE***OUTCOMPUTERSCIENCE*EFENSI*ECOMPETITIONS*REOFTEN***ORIOUS*FF*IRS*N*COME*O*NTORUNNIN*C*EC**ISTS*N*E*ECUTIN*CONFI*SCRIPTSOFFENSEONT*EOT*ER**N*IS*E**I*YFOCUSE*ONE*P*OR*TION*N*IMPRO*IS*TION*N*OFTEN**SE*EMENTSOFP**Y*E*E*IE*E*COMPETITIONTOUC*IN*ONT*EOFFENSI*EE*EMENTSOFCOMPUTERSECURITYIST*EREFORE**ETTER*E*IC*EFORTEC*E**N*E*ISMTOSTU*ENTSIN*MERIC*N*I**SC*OO*SFURT*ER*E*E*IE*ET**T*NUN*ERST*N*IN*OFOFFENSI*ETEC*NI*UESISESSENTI**FORMOUNTIN**NEFFECTI*E*EFENSE*N*T**TT*ETOO*S*N*CONFI*UR*TIONFOCUSENCOUNTERE*IN*EFENSI*ECOMPETITIONS*OESNOT*E**STU*ENTSTO*NO*T*EIRENEMY*SEFFECTI*E*Y*STE*C*IN*T*EMTO*CTI*E*YT*IN**I*E*N*TT*C*ERPICOCTFIS*NOFFENSI*E*YORIENTE**I**SC*OO*COMPUTERSECURITYCOMPETITIONT**TSEE*STO*ENER*TEINTERESTINCOMPUTERSCIENCE*MON**I**SC*OO*ERSTE*C*IN*T*EMENOU****OUTCOMPUTERSECURITYTOPI*UET*EIRCURIOSITYMOTI**TIN*T*EMTOE*P*OREONT*EIRO*N*N*EN***IN*T*EMTO*ETTER*EFEN*T*EIRM*C*INEST*EF***ISPICOCTF{N6R4M_4N41Y515_15_73*10U5_8E1*F808}
```

The two first words, ```T*EREE*IST```, jump out now as "THEREEXIST".

* ```nafyffoxen --> T*EREE*IST``` (Possibly "THEREEXIST")

New mappings: "a" to "H", "o" to "X".

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | H        |
| B          | --><-- | ?        |
| C          | --><-- | ?        |
| D          | --><-- | ?        |
| E          | --><-- | S        |
| F          | --><-- | E        |
| G          | --><-- | M        |
| H          | --><-- | Y        |
| I          | --><-- | ?        |
| J          | --><-- | ?        |
| K          | --><-- | ?        |
| L          | --><-- | N        |
| M          | --><-- | ?        |
| N          | --><-- | T        |
| O          | --><-- | X        |
| P          | --><-- | ?        |
| Q          | --><-- | O        |
| R          | --><-- | ?        |
| S          | --><-- | P        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | F        |
| W          | --><-- | U        |
| X          | --><-- | I        |
| Y          | --><-- | R        |
| Z          | --><-- | C        |

Deciphered text so far:

```
THEREEXISTSE*ER**OTHER*E**EST***ISHE*HI*HSCHOO*COMPUTERSECURITYCOMPETITIONSINC*U*IN*CY*ERP*TRIOT*N*USCY*ERCH***EN*ETHESECOMPETITIONSFOCUSPRIM*RI*YONSYSTEMS**MINISTR*TIONFUN**MENT**S*HICH*RE*ERYUSEFU**N*M*R*ET***ES*I**SHO*E*ER*E*E*IE*ETHEPROPERPURPOSEOF*HI*HSCHOO*COMPUTERSECURITYCOMPETITIONISNOTON*YTOTE*CH***U***ES*I**S*UT**SOTO*ETSTU*ENTSINTERESTE*IN*N*EXCITE***OUTCOMPUTERSCIENCE*EFENSI*ECOMPETITIONS*REOFTEN***ORIOUS*FF*IRS*N*COME*O*NTORUNNIN*CHEC**ISTS*N*EXECUTIN*CONFI*SCRIPTSOFFENSEONTHEOTHERH*N*ISHE**I*YFOCUSE*ONEXP*OR*TION*N*IMPRO*IS*TION*N*OFTENH*SE*EMENTSOFP**Y*E*E*IE*E*COMPETITIONTOUCHIN*ONTHEOFFENSI*EE*EMENTSOFCOMPUTERSECURITYISTHEREFORE**ETTER*EHIC*EFORTECHE**N*E*ISMTOSTU*ENTSIN*MERIC*NHI*HSCHOO*SFURTHER*E*E*IE*ETH*T*NUN*ERST*N*IN*OFOFFENSI*ETECHNI*UESISESSENTI**FORMOUNTIN**NEFFECTI*E*EFENSE*N*TH*TTHETOO*S*N*CONFI*UR*TIONFOCUSENCOUNTERE*IN*EFENSI*ECOMPETITIONS*OESNOT*E**STU*ENTSTO*NO*THEIRENEMY*SEFFECTI*E*Y*STE*CHIN*THEMTO*CTI*E*YTHIN**I*E*N*TT*C*ERPICOCTFIS*NOFFENSI*E*YORIENTE*HI*HSCHOO*COMPUTERSECURITYCOMPETITIONTH*TSEE*STO*ENER*TEINTERESTINCOMPUTERSCIENCE*MON*HI*HSCHOO*ERSTE*CHIN*THEMENOU*H**OUTCOMPUTERSECURITYTOPI*UETHEIRCURIOSITYMOTI**TIN*THEMTOEXP*OREONTHEIRO*N*N*EN***IN*THEMTO*ETTER*EFEN*THEIRM*CHINESTHEF***ISPICOCTF{N6R4M_4N41Y515_15_73*10U5_8E1*F808}
```

Still focusing on the first words in the ciphertext a couple others stand out, such as ```SE*ER**``` and ```HI*HSCHOO*``` which are probably the words "SEVERAL" and "HIGHSCHOOL".

* ```efufytp --> SE*ER**``` (Possibly "SEVERAL")

* ```axraezaqqp --> HI*HSCHOO*``` (Possibly "HIGHSCHOOL")

New mappings: "u" to "V", "t" to "A", "p" to "L", and "r" to "G".

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | H        |
| B          | --><-- | ?        |
| C          | --><-- | ?        |
| D          | --><-- | ?        |
| E          | --><-- | S        |
| F          | --><-- | E        |
| G          | --><-- | M        |
| H          | --><-- | Y        |
| I          | --><-- | ?        |
| J          | --><-- | ?        |
| K          | --><-- | ?        |
| L          | --><-- | N        |
| M          | --><-- | ?        |
| N          | --><-- | T        |
| O          | --><-- | X        |
| P          | --><-- | L        |
| Q          | --><-- | O        |
| R          | --><-- | G        |
| S          | --><-- | P        |
| T          | --><-- | A        |
| U          | --><-- | V        |
| V          | --><-- | F        |
| W          | --><-- | U        |
| X          | --><-- | I        |
| Y          | --><-- | R        |
| Z          | --><-- | C        |

Deciphered text so far:

```
THEREEXISTSEVERALOTHER*ELLESTA*LISHE*HIGHSCHOOLCOMPUTERSECURITYCOMPETITIONSINCLU*INGCY*ERPATRIOTAN*USCY*ERCHALLENGETHESECOMPETITIONSFOCUSPRIMARILYONSYSTEMSA*MINISTRATIONFUN*AMENTALS*HICHAREVERYUSEFULAN*MAR*ETA*LES*ILLSHO*EVER*E*ELIEVETHEPROPERPURPOSEOFAHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONISNOTONLYTOTEACHVALUA*LES*ILLS*UTALSOTOGETSTU*ENTSINTERESTE*INAN*EXCITE*A*OUTCOMPUTERSCIENCE*EFENSIVECOMPETITIONSAREOFTENLA*ORIOUSAFFAIRSAN*COME*O*NTORUNNINGCHEC*LISTSAN*EXECUTINGCONFIGSCRIPTSOFFENSEONTHEOTHERHAN*ISHEAVILYFOCUSE*ONEXPLORATIONAN*IMPROVISATIONAN*OFTENHASELEMENTSOFPLAY*E*ELIEVEACOMPETITIONTOUCHINGONTHEOFFENSIVEELEMENTSOFCOMPUTERSECURITYISTHEREFOREA*ETTERVEHICLEFORTECHEVANGELISMTOSTU*ENTSINAMERICANHIGHSCHOOLSFURTHER*E*ELIEVETHATANUN*ERSTAN*INGOFOFFENSIVETECHNI*UESISESSENTIALFORMOUNTINGANEFFECTIVE*EFENSEAN*THATTHETOOLSAN*CONFIGURATIONFOCUSENCOUNTERE*IN*EFENSIVECOMPETITIONS*OESNOTLEA*STU*ENTSTO*NO*THEIRENEMYASEFFECTIVELYASTEACHINGTHEMTOACTIVELYTHIN*LI*EANATTAC*ERPICOCTFISANOFFENSIVELYORIENTE*HIGHSCHOOLCOMPUTERSECURITYCOMPETITIONTHATSEE*STOGENERATEINTERESTINCOMPUTERSCIENCEAMONGHIGHSCHOOLERSTEACHINGTHEMENOUGHA*OUTCOMPUTERSECURITYTOPI*UETHEIRCURIOSITYMOTIVATINGTHEMTOEXPLOREONTHEIRO*NAN*ENA*LINGTHEMTO*ETTER*EFEN*THEIRMACHINESTHEFLAGISPICOCTF{N6R4M_4N41Y515_15_73*10U5_8E1*F808}
```

Again foucing on the first words, ```*ELLESTA*LISHE*```, sticks out as possibly being "WELLESTABLISHED".

```mfppfentkpxeafb --> *ELLESTA*LISHE*``` (Possibly "WELLESTABLISHED")

New mappings: "m" to "W", "k" to "B", and "b" to "D".

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | H        |
| B          | --><-- | D        |
| C          | --><-- | ?        |
| D          | --><-- | ?        |
| E          | --><-- | S        |
| F          | --><-- | E        |
| G          | --><-- | M        |
| H          | --><-- | Y        |
| I          | --><-- | ?        |
| J          | --><-- | ?        |
| K          | --><-- | B        |
| L          | --><-- | N        |
| M          | --><-- | W        |
| N          | --><-- | T        |
| O          | --><-- | X        |
| P          | --><-- | L        |
| Q          | --><-- | O        |
| R          | --><-- | G        |
| S          | --><-- | P        |
| T          | --><-- | A        |
| U          | --><-- | V        |
| V          | --><-- | F        |
| W          | --><-- | U        |
| X          | --><-- | I        |
| Y          | --><-- | R        |
| Z          | --><-- | C        |

Deciphered text so far:

```
THEREEXISTSEVERALOTHERWELLESTABLISHEDHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONSINCLUDINGCYBERPATRIOTANDUSCYBERCHALLENGETHESECOMPETITIONSFOCUSPRIMARILYONSYSTEMSADMINISTRATIONFUNDAMENTALSWHICHAREVERYUSEFULANDMAR*ETABLES*ILLSHOWEVERWEBELIEVETHEPROPERPURPOSEOFAHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONISNOTONLYTOTEACHVALUABLES*ILLSBUTALSOTOGETSTUDENTSINTERESTEDINANDEXCITEDABOUTCOMPUTERSCIENCEDEFENSIVECOMPETITIONSAREOFTENLABORIOUSAFFAIRSANDCOMEDOWNTORUNNINGCHEC*LISTSANDEXECUTINGCONFIGSCRIPTSOFFENSEONTHEOTHERHANDISHEAVILYFOCUSEDONEXPLORATIONANDIMPROVISATIONANDOFTENHASELEMENTSOFPLAYWEBELIEVEACOMPETITIONTOUCHINGONTHEOFFENSIVEELEMENTSOFCOMPUTERSECURITYISTHEREFOREABETTERVEHICLEFORTECHEVANGELISMTOSTUDENTSINAMERICANHIGHSCHOOLSFURTHERWEBELIEVETHATANUNDERSTANDINGOFOFFENSIVETECHNI*UESISESSENTIALFORMOUNTINGANEFFECTIVEDEFENSEANDTHATTHETOOLSANDCONFIGURATIONFOCUSENCOUNTEREDINDEFENSIVECOMPETITIONSDOESNOTLEADSTUDENTSTO*NOWTHEIRENEMYASEFFECTIVELYASTEACHINGTHEMTOACTIVELYTHIN*LI*EANATTAC*ERPICOCTFISANOFFENSIVELYORIENTEDHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONTHATSEE*STOGENERATEINTERESTINCOMPUTERSCIENCEAMONGHIGHSCHOOLERSTEACHINGTHEMENOUGHABOUTCOMPUTERSECURITYTOPI*UETHEIRCURIOSITYMOTIVATINGTHEMTOEXPLOREONTHEIROWNANDENABLINGTHEMTOBETTERDEFENDTHEIRMACHINESTHEFLAGISPICOCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}
```

```MAR*ETABLES*ILLS``` stands out as "MARKETABLESKILLS".

```gtycfntkpfecxppe --> MAR*ETABLES*ILLS``` (Possibly "MARKETABLESKILLS")

New mappings: "c" to "K".

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | H        |
| B          | --><-- | D        |
| C          | --><-- | K        |
| D          | --><-- | ?        |
| E          | --><-- | S        |
| F          | --><-- | E        |
| G          | --><-- | M        |
| H          | --><-- | Y        |
| I          | --><-- | ?        |
| J          | --><-- | ?        |
| K          | --><-- | B        |
| L          | --><-- | N        |
| M          | --><-- | W        |
| N          | --><-- | T        |
| O          | --><-- | X        |
| P          | --><-- | L        |
| Q          | --><-- | O        |
| R          | --><-- | G        |
| S          | --><-- | P        |
| T          | --><-- | A        |
| U          | --><-- | V        |
| V          | --><-- | F        |
| W          | --><-- | U        |
| X          | --><-- | I        |
| Y          | --><-- | R        |
| Z          | --><-- | C        |

Deciphered text so far:

```
THEREEXISTSEVERALOTHERWELLESTABLISHEDHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONSINCLUDINGCYBERPATRIOTANDUSCYBERCHALLENGETHESECOMPETITIONSFOCUSPRIMARILYONSYSTEMSADMINISTRATIONFUNDAMENTALSWHICHAREVERYUSEFULANDMARKETABLESKILLSHOWEVERWEBELIEVETHEPROPERPURPOSEOFAHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONISNOTONLYTOTEACHVALUABLESKILLSBUTALSOTOGETSTUDENTSINTERESTEDINANDEXCITEDABOUTCOMPUTERSCIENCEDEFENSIVECOMPETITIONSAREOFTENLABORIOUSAFFAIRSANDCOMEDOWNTORUNNINGCHECKLISTSANDEXECUTINGCONFIGSCRIPTSOFFENSEONTHEOTHERHANDISHEAVILYFOCUSEDONEXPLORATIONANDIMPROVISATIONANDOFTENHASELEMENTSOFPLAYWEBELIEVEACOMPETITIONTOUCHINGONTHEOFFENSIVEELEMENTSOFCOMPUTERSECURITYISTHEREFOREABETTERVEHICLEFORTECHEVANGELISMTOSTUDENTSINAMERICANHIGHSCHOOLSFURTHERWEBELIEVETHATANUNDERSTANDINGOFOFFENSIVETECHNI*UESISESSENTIALFORMOUNTINGANEFFECTIVEDEFENSEANDTHATTHETOOLSANDCONFIGURATIONFOCUSENCOUNTEREDINDEFENSIVECOMPETITIONSDOESNOTLEADSTUDENTSTOKNOWTHEIRENEMYASEFFECTIVELYASTEACHINGTHEMTOACTIVELYTHINKLIKEANATTACKERPICOCTFISANOFFENSIVELYORIENTEDHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONTHATSEEKSTOGENERATEINTERESTINCOMPUTERSCIENCEAMONGHIGHSCHOOLERSTEACHINGTHEMENOUGHABOUTCOMPUTERSECURITYTOPI*UETHEIRCURIOSITYMOTIVATINGTHEMTOEXPLOREONTHEIROWNANDENABLINGTHEMTOBETTERDEFENDTHEIRMACHINESTHEFLAGISPICOCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}
```

```TECHNI*UES``` stands out as "TECHNIQUES".





```nfzalxiwfe --> TECHNI*UES``` (Possibly "TECHNIQUES")

New mappings: "i" to "Q".

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | H        |
| B          | --><-- | D        |
| C          | --><-- | K        |
| D          | --><-- | ?        |
| E          | --><-- | S        |
| F          | --><-- | E        |
| G          | --><-- | M        |
| H          | --><-- | Y        |
| I          | --><-- | Q        |
| J          | --><-- | ?        |
| K          | --><-- | B        |
| L          | --><-- | N        |
| M          | --><-- | W        |
| N          | --><-- | T        |
| O          | --><-- | X        |
| P          | --><-- | L        |
| Q          | --><-- | O        |
| R          | --><-- | G        |
| S          | --><-- | P        |
| T          | --><-- | A        |
| U          | --><-- | V        |
| V          | --><-- | F        |
| W          | --><-- | U        |
| X          | --><-- | I        |
| Y          | --><-- | R        |
| Z          | --><-- | C        |

Deciphered text so far:

```
THEREEXISTSEVERALOTHERWELLESTABLISHEDHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONSINCLUDINGCYBERPATRIOTANDUSCYBERCHALLENGETHESECOMPETITIONSFOCUSPRIMARILYONSYSTEMSADMINISTRATIONFUNDAMENTALSWHICHAREVERYUSEFULANDMARKETABLESKILLSHOWEVERWEBELIEVETHEPROPERPURPOSEOFAHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONISNOTONLYTOTEACHVALUABLESKILLSBUTALSOTOGETSTUDENTSINTERESTEDINANDEXCITEDABOUTCOMPUTERSCIENCEDEFENSIVECOMPETITIONSAREOFTENLABORIOUSAFFAIRSANDCOMEDOWNTORUNNINGCHECKLISTSANDEXECUTINGCONFIGSCRIPTSOFFENSEONTHEOTHERHANDISHEAVILYFOCUSEDONEXPLORATIONANDIMPROVISATIONANDOFTENHASELEMENTSOFPLAYWEBELIEVEACOMPETITIONTOUCHINGONTHEOFFENSIVEELEMENTSOFCOMPUTERSECURITYISTHEREFOREABETTERVEHICLEFORTECHEVANGELISMTOSTUDENTSINAMERICANHIGHSCHOOLSFURTHERWEBELIEVETHATANUNDERSTANDINGOFOFFENSIVETECHNIQUESISESSENTIALFORMOUNTINGANEFFECTIVEDEFENSEANDTHATTHETOOLSANDCONFIGURATIONFOCUSENCOUNTEREDINDEFENSIVECOMPETITIONSDOESNOTLEADSTUDENTSTOKNOWTHEIRENEMYASEFFECTIVELYASTEACHINGTHEMTOACTIVELYTHINKLIKEANATTACKERPICOCTFISANOFFENSIVELYORIENTEDHIGHSCHOOLCOMPUTERSECURITYCOMPETITIONTHATSEEKSTOGENERATEINTERESTINCOMPUTERSCIENCEAMONGHIGHSCHOOLERSTEACHINGTHEMENOUGHABOUTCOMPUTERSECURITYTOPIQUETHEIRCURIOSITYMOTIVATINGTHEMTOEXPLOREONTHEIROWNANDENABLINGTHEMTOBETTERDEFENDTHEIRMACHINESTHEFLAGISPICOCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}
```

After adding spaces:

```
THERE EXIST SEVERAL OTHER WELL ESTABLISHED HIGHSCHOOL COMPUTER SECURITY COMPETITIONS INCLUDING CYBER PATRIOT AND US CYBER CHALLENGE THESE COMPETITIONS FOCUS PRIMARILY ON SYSTEMS ADMINISTRATION FUNDAMENTALS WHICH ARE VERY USEFUL AND MARKETABLE SKILLS HOWEVER WE BELIEVE THE PROPER PURPOSE OF A HIGHSCHOOL COMPUTER SECURITY COMPETITION IS NOT ONLY TO TEACH VALUABLE SKILLS BUT ALSO TO GET STUDENTS INTERESTED IN AND EXCITED ABOUT COMPUTER SCIENCE DEFENSIVE COMPETITIONS ARE OFTEN LABORIOUS AFFAIRS AND COME DOWN TO RUNNING CHECKLISTS AND EXECUTING CONFIG SCRIPTS OFFENSE ON THE OTHER HAND IS HEAVILY FOCUSED ON EXPLORATION AND IMPROVISATION AND OFTEN HAS ELEMENTS OF PLAY WE BELIEVE A COMPETITION TOUCHING ON THE OFFENSIVE ELEMENTS OF COMPUTER SECURITY IS THEREFORE A BETTER VEHICLE FOR TECH EVANGELISM TO STUDENTS IN AMERICAN HIGHSCHOOLS FURTHER WE BELIEVE THAT AN UNDERSTANDING OF OFFENSIVE TECHNIQUES IS ESSENTIAL FOR MOUNTING AN EFFECTIVE DEFENSE AND THAT THE TOOLS AND CONFIGURATION FOCUS ENCOUNTERED IN DEFENSIVE COMPETITIONS DOES NOT LEAD STUDENTS TO KNOW THEIR ENEMY AS EFFECTIVELY AS TEACHING THEM TO ACTIVELY THINK LIKE AN ATTACKER PICOCTF IS AN OFFENSIVELY ORIENTED HIGHSCHOOL COMPUTER SECURITY COMPETITION THAT SEEKS TO GENERATE INTEREST IN COMPUTER SCIENCE AMONG HIGHSCHOOLERS TEACHING THEM ENOUGH ABOUT COMPUTER SECURITY TO PIQUE THEIR CURIOSITY MOTIVATING THEM TO EXPLORE ON THEIR OWN AND ENABLING THEM TO BETTER DEFEND THEIR MACHINES THE FLAG IS PICOCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}
```

Finally, we fully uncover the hidden message and flag.

```PICOCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}```
