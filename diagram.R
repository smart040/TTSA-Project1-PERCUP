x=1:5
y=rep(3,5)
plot(x,y,col='red',type = 'l',ylim = c(1.5,3.5), axes = FALSE, frame.plot = TRUE)
lines(c(2:4),y=c(2,2,2),col='blue')
abline(v=4,lty=2)
abline(v=5,lty=2)
legend(x=4.1,y=2.9,latex2exp::TeX('$\\varphi_{|\\alpha}$'),box.col = 'white')
legend(x=2.0,y=2,latex2exp::TeX('$\\psi$'),box.col = 'white')

