PLAYER_NAME='fatant'
f,t,s=0,[],"""$;SCT(/;S[T&)$;SC$&)$;SC$&)/;#GD'L@]7-X'R;_/,/,5M:JRQ@>_VF@SSQAT5YF*5G+4E',5G+4E',5G+4EW#NFaE-8]T&&?1*)RA6FMSL;(:NF:DD;,E4S:*A('S6''+)ECW0APCSC*&+&T'9:1U%a]D',5G+4E',5G+<QVI?>(EH7T?D*2E',5G+4E',5G+4U'2A][.*&KS\\&\\,P*5G+4E',5G+4EG,A_-S2[8,;*C$&)$;SC$&)/;SC$&)/;SG>6CZKS#/:T`A%CAB(A>V&E*2A_[T6*bCG,LMaSL&6(5XC$G+T:b#A_7R9*2A$T=%aNSQ7@=S>'G+4E',6]/TF*2A_*IA'I=F)EU%L4.+:5#)/;Y3U'2A_[.K/MT%+R\\)(5G+4E7)`]+4EG,A_[T2#9W<40Q.DO+)#O/6E5TSF*R%_[TF:3RR*.CO#NWI4I15]AK3&H05_CSF*R$&%)W(#GT,-##$%5*7$_C8Y.TF*2A&B(1KL32a=I)<=&+(E/05G+4E',UH)]-4SDE?BE+4=D+`EX.%Y.6OG0>YO._@)8A&23(=VI+4)<+5S1#JI0>YO<>[N3M26AC-8J*3E/ED67N5`.8NO<V9S/17@IW\\$MB:/0\\3HBbE5<-SCN%)_#A`A-5K*M#K1($5'-4_`#XRC$&I-X$U/3095M5HA;9VL%LAKV6M7L5H-8M'/3C-NG5>9+=UL#3-G-8M,L5H-8M7*?U#8K,L-4-8M*']1L7M*K5H-8M7L1S3$M5650]D&6L17$8M723H-8M7L5@#U%TGI'=79123(<V]723H-8M7L5H]#72L=%\\7M`I5(L$G-3=C-5G,L1(,U$+$C%=5L3>A-L3G+(5J-X&+65H-XL&_0KCVF74YF=7G)2E7T7D,4I/,5G+*;C3/K*H-(\\7F+4IWC3Z64E?-5G+45#)$M1(UFZ1J_3AG*U@,K-0\\$M5L1@S.%SE<7]Q@_Y,^KD;_#3B+FA_[TFZC:'+#V+RK'AQ&I/FT-O6TT%_YSF*R$V+#&I46SC$.9W;`#SFZ0WS[8C*2A&A4#)/FIE%.-/;)^$&)/;*C@F*/;S)/6&/;)0$N77;S3a%Y.;'%0)Y1;SC4;'#;S/9%)/;SC,N+/;SC$&$/;S+#>S/5SC<O'/;SC$&YN:S+#&).\\SC$^X#4#A`5;L5HC$&)O:G+8%),5*C4C'L$?+_%I45G-8EW.5G+4M'O5G;@I'L$&[/#9L$G+4+-,&(20C7L$R+0[#,#G'S<#$;&)7ECC4&)3=CC/&)3=##D&'+3#$%>'+#&$%;)+#F#$;'+#&$$*'+3C/#'?$3#)#%?$3#)#%S#3#)#%O'5C#&#'+#C#$#'+#C#$#'+#C#$#'+3DC#%#'K##$$#+3##$$#+;#C$&#'+#CZ$##+###$##+###$##+###$##+###-#############################"""
for x in range(len(s)):
 m=ord(s[x])-35
 y=x%7
 f+=(m%(1<<y))<<(7-y)%7
 if y>0:t+=[f//11,f%11]
 f=m>>y
t+=[f//11,f%11]
def final_strategy(a,b):
 return t[min(a,49)*50+min(b,49)]