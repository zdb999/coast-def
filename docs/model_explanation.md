# Model Explanation

## Sea level

### An example of what we can do

To create the “Intermediate High” projection, the orange line in Figure 1, the CPO-1 report averaged the results of Vermeer and Rahmstorf (2009) and Grinsted et al. (2009). They then approximated the time evolution by a quadratic function

\[ E(t)=m\left(t-t_{0}\right)+b\left(t-t_{0}\right)^{2} \]

where \(t_{0}=1992\), \(m=1.7\ltimes10^{3}\),and \(b=8.71\ltimes10^{-5}\). Adapting this for Conneticut's subsistence rate to get produces 

\[ E(t)=\left(0.0007+m\right)\left(t-t_{0}\right)+b\left(t-t_{0}\right)^{2} \]

## Storm surge

## Risk aversion

Here's a good [site](https://saylordotorg.github.io/text_introduction-to-economic-analysis/s14-04-risk-aversion.html).

The common practice of government entities when assessing disaster mitigation is to run a cost benefit anaylsis assuming risk neutrality and allocate funding efficiently on that basis. This risk neutral approach is easily justifiable because it allows for funds to be equitably allocated so that every dollar spent on disaster prevention is used to prevent destruction of value. However, this is not consistant with the concept of social welfare. The cost benefit analysis focuses on the monetary damages to property rather than the effects on communities and other intangibles. In order to more properly represent the true benefit of preventing flood damage more tools are needed than a simple household price and damage. Our model aims to take a risk averse approach to considering the damages associated with flooding while justifying investment in infrastructure. 
	Our risk aversion analysis draws heavily from the paper conducted by Attanasi and Karlinger “Risk Preferences and Flood Insurance”. In this paper, the authors discuss and conclude that when it comes to insuring for flood damages people are risk averse. Furthermore, they use the Von-Neumann Morgenstein expected-utility model to analyze the significance of the consumers’ choices. 

Our risk aversion analysis draws heavily from the paper conducted by Attanasi and Karlinger “Risk Preferences and Flood Insurance”
(https://www.jstor.org/stable/1239435?seq=1#metadata_info_tab_contents). In this paper, the authors discuss and conclude that when it comes to insuring for flood damages people are definitely risk averse. In order to quantify this relationship, they use the Von-Neumann Morgenstein expected-utility model to analyze the significance of the consumers’ choices. 

The greatest challenge of quantifying risk aversion comes from the sometimes irrational behavior of individuals. In these two paper (Insert citation), the authors establish that individuals struggle to comprehend the damage that can be associated with very destructive infrequent storms. This irrational behavior leads to results that often do not match the hypothesis of the Von-Neumann Morgenstein expected-utility model. However, the goal of Coast-Def is to rationally assess the damages and weigh the potential benefit from investing significantly in infrastructure. 

The wealth functions considered are as follows. The variables are defined as follows: $W$ is the final wealth of the individual as expressed in the equation, $A$ is the value of assets not subject to loss in the event of a flood, $L$ the maximum value of assets that are subject to loss in the event of a flood, $C$ the amount of coverage that the insurance company has agreed to provide, $P$ the premium of the policy, $X$ the random damages associated with a hazard event


$$ W_{0}=A+L-PC; X=0$$

$$ W_{1}=A+L-PC-X; 0<X<200 $$

$$ W_{2}=A+L-PC-200; 200<X≤10,000 $$

$$ W_{3}=A+L-PC-0.02X; 10,000<X<C<L $$

$$ W_{4}=A+L-PC-0.02X-(X-C); 10,000<C≤X<L $$

$$ E[U(Y)=(1-exp\{-\alpha W_{0}[X(Q_{0})]\})k_{1} $$

$$ +\intop_{Q_{a}}^{Q_{b}}(1-exp\{\alpha W_{2}[X(Q)]\})f(Q)dQ $$

$$ +\intop_{Q_{b}}^{Q_{c}}(1-exp\{-\alpha W_{3}[X(Q)]\})f(Q)dQ $$

$$ +\intop_{Q_{c}}^{Q_{T}}(1-exp\{\alpha W_{4}[X(Q)]\})f(Q)dQ $$

$$ +(1-exp\{-\alpha W_{4}[X(Q)]\})k_{2} $$

This equation expressing the calculation of utility consider $k_{1}$ as the probability the discharges lsss than $Q_{0}$. $k_{2}$ being the probability the discharge is greater than $Q_{T}$. 

We have decided from the research presented above to use a Von-Neumann Morgenstein expected-utility model to consider risk aversion. This means that we plan on assigning a monetary value to the inconvenience and cost of relocating after a flood disaster.


## Present Value Calculations

One of the most important features of any model aiming to include a cost benefit analysis is to be able to calculate the value of future costs and benefits in an easily understandable and comparable way. For this project we have decided to use a yearly discounting model to calculate these values. 

$$ P[\frac{1-(1+r)^{-n})}{r}] $$

$ P = value per Year $

$ r = annual discount rate $

$ n = number of years $

Here's a good [site](http://financeformulas.net/Present_Value_of_Annuity.html). Using this formula, we can create a present value for all of the future costs and benefits of investing in infrastructure. This calculation makes it possible to consider benefit over a long period of time compared to the cost of construction today. There are still many other considerations one must take when deciding upon an interest rate and useful life of the infrastructure which factor heavily into this calculation.
