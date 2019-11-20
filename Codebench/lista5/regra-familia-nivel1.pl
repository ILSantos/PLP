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
% predicados

pai(P,F) :- mae(M,F), casal(P,M).
pais(P,F) :- mae(P,F) | pai(P,F).

%%%%%%%%%%
% Inserir na base as seguintes regras:
% A regra pai(P, F) deve unificar P e F se P for o pai de F;
% A regra pais(P, F) deve unificar P e F se P for pai ou mãe de F;
% A regra irmaos(A, B) deve unificar A e B se eles forem irmãos, independentemente do gênero;
% A regra irma(M, X) deve unificar M e X se eles forem irmãos e M for mulher;
% A regra irmao(H, X) deve unificar H e X se eles forem irmãos e H for homem;
% A regra avo(V, N) deve unificar V e N se V for o avô de N, independentemente dos gêneros;
% As regra avo_paterno(V, N) e avo_materno(V, N) devem unificar V e N se houver relação de avô e neto entre eles, independentemente dos gêneros. Porém as regras devem diferir com respeito ao pai ou mãe. Por exemplo, lucretia não possui avós maternos, de acordo com a base, porém seus avós paternos são great_sirius e hesper (os pais de arcturus_II).

% Escrever as consultas: 

% Quem é o pai de harry?
% Quem são os filhos de harry?
% Quem são os irmãos (e irmãs) de ronny?
% Quem são os irmãos (homens) de ronny?
% Quem são as irmãs de andromeda?
% Quem são os avôs de george?
% Quem são os avôs paternos de roxanne?
% Quem são os avôs (homens) de george? (Dica: use uma conjunção na sua consulta)
% Quem é a bisavó de bellatrix?

%%%%% Consultas
%
%
% Descreva aqui as consultas que voce usou
% para testar sua base de conhecimento
%
%
