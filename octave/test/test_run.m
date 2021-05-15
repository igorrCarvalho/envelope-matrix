addpath('../src');
addpath('../src/envelopeLuDecomposition');

clear all

load A.mat
load b.mat;

n = size(A)(2);

enveTriL = envelopeBuild(tril(A)');
enveTriU = envelopeBuild(triu(A));

uA = envelopeUnwrap(enveTriL)';
uA = uA + envelopeUnwrap(enveTriU) - diag(uA) .* eye(n);
sum(sum(A - uA))

[L, U] = envelopeLuDecomposition(enveTriL, enveTriU);

y = envelopeForwardSubstitution(L, b);
x = envelopeBackwardSubstitution(U, y);

x_ = A \ b;
norm(x_ - x) / norm(x)
