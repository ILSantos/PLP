%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
% Base de conhecimento
%

% Todos os nomes
homem(great_sirius).
homem(phineas).
homem(sirius).
homem(cygnus).
homem(arcturus).
homem(arcturus_II).
homem(pollux).
homem(ignatius).
homem(mr_prewett).
homem(orion).
homem(cygnus_II).
homem(septimus).
homem(arthur).
homem(gideon).
homem(sirius).
homem(regulus).
homem(rodolphus).
homem(ted).
homem(james_potter).
homem(vernon).
homem(dudley).
homem(percy).
homem(george).
homem(fred).
homem(ronny).
homem(harry).
homem(fred_II).
homem(hugo).
homem(james_sirius).
homem(albus_severus).
mulher(cassiopeia).
mulher(cedrella).
mulher(lucretia).
mulher(great_ms_prewett).
mulher(walburga).
mulher(ms_prewett).
mulher(angelina).
mulher(druella).
mulher(molly).
mulher(lily_evans).
mulher(bellatrix).
mulher(andromeda).
mulher(nymphadora).
mulher(ms_evans).
mulher(ms_dursley).
mulher(petunia).
mulher(marjorie).
mulher(audrey).
mulher(hermione).
mulher(ginny).
mulher(lucy).
mulher(roxanne).
mulher(molly_daughter).
mulher(rose).
mulher(lily_potter).
mulher(irma).
mulher(melania).
mulher(lysandra).
mulher(violetta).
mulher(hesper).
mulher(ursula).

% mae
% Primeira geracao
mae(ursula, sirius).
mae(ursula, cygnus).
mae(ursula, arcturus).

% Segunda geracao
mae(hesper, arcturus_II).
mae(violetta, pollux).
mae(violetta, cassiopeia).
mae(lysandra, cedrella).

% Terceira geracao
mae(melania, lucretia).
mae(melania, orion).
mae(irma, walburga).
mae(irma, cygnus_II).
mae(great_ms_prewett, ms_prewett).

% Quarta geracao (os adultos)
mae(ms_prewett, molly).
mae(ms_prewett, gideon).
mae(cedrella, arthur).
mae(walburga, sirius).
mae(walburga, regulus).
mae(druella, bellatrix).
mae(druella, andromeda).
mae(ms_evans, lily_evans).
mae(ms_evans, petunia).
mae(ms_dursley, vernon).
mae(ms_dursley, marjorie).

% Quinta geracao (os protagonistas)
mae(molly, percy).
mae(molly, george).
mae(molly, fred).
mae(molly, ronny).
mae(molly, ginny).
mae(lily_evans, harry).
mae(petunia, dudley).
mae(andromeda, nymphadora).

% Sexta geracao (os filhos)
mae(audrey, molly_daughter).
mae(audrey, lucy).
mae(angelina, fred_II).
mae(angelina, roxanne).
mae(hermione, rose).
mae(hermione, hugo).
mae(ginny, james_sirius).
mae(ginny, albus_severus).
mae(ginny, lily_potter).

% casal/2
% Primeira geracao
casal(phineas, ursula).

% Segundaga geracao
casal(great_sirius, hesper).
casal(cygnus, violetta).
casal(arcturus, lysandra).

% Terceira geracao
casal(arcturus_II, melania).
casal(pollux, irma).

% Quarta geracao
casal(ignatius, lucretia).
casal(mr_prewett, ms_prewett).
casal(orion, walburga).
casal(cygnus_II, druella).
casal(septimus, cedrella).

% Quinta geracao (pais dos protagonistas)
casal(arthur, molly).
casal(rodolphus, bellatrix).
casal(james_potter, lily_evans).
casal(vernon, petunia).
casal(rodolphus, bellatrix).
casal(ted, andromeda).

% Quinta geracao (os protagonistas)
casal(percy, audrey).
casal(george, angelina).
casal(ronny, hermione).
casal(harry, ginny).

% Remova este comentario e escreva aqui seus
pai(P,F) :- mae(M,F), casal(P,M).
pais(P,F) :- mae(P, F) | pai(P,F).
irmaos(A, B) :- mae(M,A) , mae(M,B), A\=B.
irma(M,X) :- irmaos(M,X), mulher(X).
irmao(H,X) :- irmaos(H,X), homem(X).
avo(V,N) :- pais(V,X) , pais(X,N).
avo_paterno(V,N) :- pais(V,X), pais(X,N), homem(X).
avo_materno(V,N) :- pais(V,X), pais(X,N), mulher(X).

tio(T,S) :- irmaos(T, X), pais(X, S), homem(T).
tio(T,S) :- casal(T, X), irmaos(X,C), pais(C,S), homem(T).
tia(T,S) :- irmaos(T, X), pais(X, S), mulher(T).
tia(T,S) :- casal(X, T), irmaos(X, C), pais(C,S), mulher(T).
tios(T,S) :- tio(T,S) | tia(T,S).
primos(P,X) :- tio(T,P), pais(T,X), P\=X.
primo(H,X) :- primos(H,X), homem(H).
prima(M,X) :- primos(M,X), mulher(M).
sogro(S,X) :- casal(X,T), pai(S,T).
sogro(S,X) :- casal(T,X), pai(S,T).
sogra(S,X) :- casal(X,T), mae(S,T).
sogra(S,X) :- casal(T,X), mae(S,T).
genro(G,X) :- casal(G,M), mae(X,M).
genro(G,X) :- casal(G,M), pai(X,M).
nora(N,X) :-  casal(H,N), mae(X,H).
nora(N,X) :- casal(H,N), pai(X,H).
%%%%% Consultas
% tio(X, lucy).
% tia(X, lucy).
% tia(X, rose).
% tios(X, rose).
% primo(hugo, lucy).
% primo(rose, lucy).
% prima(rose, lucy).
% prima(hugo, lucy).
%sogro(X, harry).
%sogra(X, harry).
% sogro(arthur, X).
%sogra(molly, hermione).
%sogra(arthur, hermione).
%nora(hermione, molly).
%nora(hermione, arthur).
%genro(harry, arthur).
% nora(X, arthur).
