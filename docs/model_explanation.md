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

The common practice of government entities when assessing disaster mitigation is to run a cost benefit analysis assuming risk neutrality and allocate funding efficiently on that basis. This risk neutral approach is easily justifiable because it allows for funds to be equitably allocated so that every dollar spent on disaster prevention is used to prevent destruction of a greater value.

However, this is not consistent with the concepts of social welfare and the goals of this project. The cost benefit analysis only considers the price tag associated with destruction instead of including intangibles associated with loss of property, the inconvenience of relocation, the effects on community and the disproportionate burden placed on lowering income and property owners. 

In order to more properly represent the true benefit of preventing flood damage more tools are needed than solely the household price and damage. Our model aims to take a risk averse approach to considering the damages associated with flooding while justifying investment in infrastructure. We expect this mindset to cause our model to see a greater benefit to creating infrastructure to protect communities and hopefully draw more attention to government spending on resilience developments.
	
Our risk aversion analysis draws heavily from the paper conducted by Attanasi and Karlinger [Risk Preferences and Flood Insurance](https://www.jstor.org/stable/1239435?seq=1#metadata_info_tab_contents.html). In this paper, the authors discuss and conclude that when it comes to insuring for flood damages people are definitely risk averse. In order to quantify this relationship, they use the Von-Neumann Morgenstein expected-utility model to analyze the significance of the consumers’ choices. 

The greatest challenge of quantifying risk aversion comes from the sometimes irrational behavior of individuals. In these two papers ["Limited Knowledge and Insurance Protection"](https://nehrpsearch.nist.gov/static/files/NSF/PB270524.pdf) and ["Economics, Psychology, and Protective Behavior"](https://www.jstor.org/stable/1816663?seq=1#metadata_info_tab_contents), the authors establish and walk through the explanation around why individuals struggle to comprehend the damages that can be associated with very destructive infrequent storms. As a result of their inability to fully understand the implications of infrequent storms, consumers often place a lower value on insurance and protection plans with extreme disaster relief. This means that because people are sometimes unable to rationally look at small probability and a massive payout they sometimes tend to irrationally under value that protection because of the extreme infrequency. 

This decision making produces choices do not actually match the preferences of their makers. This phenomenon leads to results that do not perfectly match the hypothesis of the Von-Neumann Morgenstein expected-utility model. While we acknowledge the inconsistencies, we stand by the the goal of the Coast-Def project which is to rationally assess damages and potential benefit of infrastructure implementation. With that in mind, we do not see it fit to place too much weight on inconsistencies that are associated with irrational behavior and instead. 

Below are wealth functions from the paper conducted by Attanasi and Karlinger [“Risk Preferences and Flood Insurance”](https://www.jstor.org/stable/1239435?seq=1#metadata_info_tab_contents). The variables are defined as follows: $W$ is the final wealth of the individual as expressed in the equation, $A$ is the value of assets not subject to loss in the event of a flood, $L$ the maximum value of assets that are subject to loss in the event of a flood, $C$ the amount of coverage that the insurance company has agreed to provide, $P$ the premium of the policy, $X$ the random damages associated with a hazard event


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

This equation expressing the calculation of utility consider $k_{1}$ as the probability the discharges are less than $ Q_{0} $. $ k_{2} $ being the probability the discharge is greater than $ Q_{T} $. 

We have decided from the research presented above to use a Von-Neumann Morgenstein expected-utility model to consider risk aversion. This means that we plan on assigning a monetary value to the inconvenience and cost of relocating after a flood disaster.

## Present Value Calculations

One of the most important features of any model aiming to include a cost benefit analysis is to be able to calculate the value of future costs and benefits in an easily understandable and comparable way. For this project we have decided to use a yearly discounting model to calculate these values. 

$$ PV=P\left[\frac{1-(1+r)^{-n})}{r}\right] $$

where $ P $ is the value per year, $ r $ is the annual discount rate, and $ n $ is number of years.

This [site](http://financeformulas.net/Present_Value_of_Annuity.html) has a simple calculator that lets you explore this equation. Using this formula, we can create a present value for all of the future costs and benefits of investing in infrastructure.

This calculation makes it possible to consider benefit over a long period of time compared to the cost of construction today. There are still many other considerations one must take when deciding upon an interest rate and useful life of the infrastructure, two parameters which factor heavily into this calculation.

## Wall Cost Calculations


Creating a cost analysis for building coastal walls can be very tricky. Many different projects have used very different approaches to predicting costs. Every project has different requirements, designs necessities, and locations. All of these factors specifically the terrain at a location can cause the cost of construction to vary greatly between difference sites or even between different spots along the same wall. For example, building a wall along a wetland causes complications when trying to set concrete into the ground that do not exist when working with dry firm soil. The added costs of better materials and more excavation work lead to increased costs and a different cost function. This variance makes it impossible to create one equation for construction costs that accurately represents all coastal wall designs. For that very reason, our dynamic model has the capability to substitute separate cost functions seamlessly in order to better represent the cost function associated with that specific projected plan. 

Examples of the various cost functions that can be used are as follows…

The model provided by professor Mendelsohn used a cost function that varied linearly with the length of the desired wall and exponentially becoming more expensive with increases in the height. The cost function was

$$ C( H,L ) = 3881.4* H 2 *L $$

The basic understanding of this function is that for every cubic meter of material required to for the wall the price increased $3,881.4. 

In a paper by Xinyu Fu and Jie Song ["Assessing the Economic Costs of Sea Level Rise and Benefits of Coastal Protection: A Spatiotemporal Approach”](https://www.mdpi.com/2071-1050/9/8/1495) used a much more complicated cost function for the development of sea walls. 

$$ PC_{S,T}^{AN}=\frac{U\text*L\text*I\text*(S+MHHW)}{T}*(101)\%%) $$

$ PC $ = protection costs given S (sea level rise) and T (projection year)

$ U $ = unit cost of building the wall

$ L $ = coastal protection ratio

$ I $ = total length of coastline for the wall to be implemented

$ S $ = sea level rise

$ MHHW $ = mean higher high water level 

This calculation serves to predict the cost of creating and maintaining a seawall on a yearly basis. The study then takes this data and creates a present value for all years by summing the values and using an annual discount factor. Shown below:

$$ PC_{S,T}^{NPV}=\sum_{t=0}^{T}PC_{S,T}^{AN}*(\frac{1}{1+r})^{t} $$


This is an example of all of the different factors that one can decide to include in their cost function. The dynamic model can then quickly input this new function and provide a new analysis based on the function.

## Household Damage Calculation

In order to know net benefit of building a wall, the damage related to surge heights must be calculated. Currently, Coast-Def calculates household flood damage as a linear function with the damage beginning when the storm surge reaches the elevation 2 meters below the house elevation. This point is marked as the lower bound for damage and conceptually represents the point at which a basement would begin to flood. Then the upper bound of damage would be 7 meters about the 1st floor elevation at which point the household would be underwater and condemned due to the massive damages

$$ Damage(\%)=\frac{(Surge-Elevation-LowerBound)}{(Upperbound-LowerBound)} $$

$ Surge $ = the elevation of the storm surge 

$ Elevation $ = the elevation relative to sea level of the first floor of the house

$ Lowerbound $= The height at which 0% of the house has been damaged

$ Upperbound $ =  The height at which 100% of the house has been damaged

This percentage is then multiplied by the total value of the house which results in the damage incurred due to a particular storm surge height. Shown below:

$$ House Value * Damage(\%) = Damage Value $$

Then the 

## Expected Marginal Benefit of a Coastal Wall

The expected marginal benefit of building a wall is the reduction in damage that comes with building a wall that would prevent a surge of the equivalent height. This can be calculated by summing all of Damage Values for every house at the particular surge level. Then multiply the damage value by the frequency (annual probability) of a surge of that height occurring. In addition, the sea level rise (SLR) per year is factored into the frequency to account for the increase in surges of a certain height every year due to the increasing sea level.

$$ E(MB)=f*\sum DamageValue $$ for all houses 

This calculation is carried out for the useful life of the wall which should be determined based on quality of materials, dimensions of the wall, terrain, and any number of other factors. Now the expected total value of creating a wall is calculated by summing together all of the marginal benefits associated with every wall height equal to or less than that particular height. 

The frequency equations are below. These equations work to estimate the frequency and probability of surges of certain heights based on data provided by local municipalities. $ k $ $ \sigma $ and $ mu $ are values that must be obtained from data collected around the area being analyzed for coastal wall implementation. It is important to note that various areas will have very different coefficients depending how prone they are to floods and many other factors. 

$$ f=1.25+1.11*(Surge-SLR)+0.25(Surge-SLR)^{2} $$ for any point where surge height is less than the inflection point plus the sea level rise due to climate change.

$$ f=e^{-1*(1+\frac{k((Surge+0.01)-(\mu+SLR))}{\sigma})^{-\frac{1}{k}}}-e^{-1*(1+\frac{k((Surge-0.01)-(\mu+SLR))}{\sigma})^{-\frac{1}{k}}} $$ for any point where surge height is greater than the inflection point plus the sea level rise due to climate change.

Now on to the Total Benefit equation. In order to find a summation of the positive changes associated with a certain wall height, all of the marginal benefits for each inch added to the wall must be added together in order to to see the total effect. 

$$ E(TB)=\sum E(MB) for all Elevations \leq the Proposed Wall Height Elevation $$

Conceptually, this summation represents adding the marginal benefit for each inch of the wall arriving at the total benefit when all of these inch segments add up to the total wall height under consideration. 

## Optimization

At this point in the process the model has produced marginal and total costs from creating walls of varying heights, lengths, and materials and also has produced a comprehensive formula for calculating marginal benefit. The most efficient wall height will occur where $ E(MB)-E(MC) = 0 $. At this point continuing to increase the wall height will cost more than value of the damage being reduced. While this is the point where the difference between total benefit and total cost is greatest, a social planner could for various reasons decide to build a wall taller than this height. Even though this would decrease the portion of the value which is considered "profit" total benefit can still be greatly increased and along with the social welfare topic discussed with risk aversion, governing bodies should consider more than just an optimum allocation when deciding how much protection to provide for a community.

The visual tool that accompanies this data anlysis provides a way to clearly see how the placement and size of walls can be justified. The combination of these two pieces truly makes this model special in its ability to allow engineers, city planners, archetects, and politicians visualization the best allocation of coastal walls.

# Sources

Attanasi, E. D., and M. R. Karlinger. “Risk Preferences and Flood Insurance.” American Journal of Agricultural Economics 61, no. 3 (1979): 490–95. [https://doi.org/10.2307/1239435](https://doi.org/10.2307/1239435).

Borsje, B. W., B. K. Van Wesenbeeck, F. Dekker, P. Paalvast, T. J. Bouma, M. M. van Katwijk, and M. B. de Vries. “How Ecological Engineering Can Serve in Coastal Protection.” 122, 2011. [https://repository.ubn.ru.nl/handle/2066/91900](https://repository.ubn.ru.nl/handle/2066/91900).

Connecticut Department of Energy & Environmental Protection. “CT ECO 2016 Imagery & Elevation.” Government Resource. University of Connecticut. Accessed December 17, 2018. [https://cteco.uconn.edu/data/flight2016/index.htm](https://cteco.uconn.edu/data/flight2016/index.htm).

Felson, Alexander. “Designed Experiments for Transformational Learning: Forging New Opportunities Through the Integration of Ecological Research Into Design.” ResearchGate. Accessed December 17, 2018.[https://www.researchgate.net/publication/318702469_Designed_Experiments_for_Transformational_Learning_Forging_New_Opportunities_Through_the_Integration_of_Ecological_Research_Into_Design](https://www.researchgate.net/publication/318702469_Designed_Experiments_for_Transformational_Learning_Forging_New_Opportunities_Through_the_Integration_of_Ecological_Research_Into_Design).

Fu and Song, “Assessing the Economic Costs of Sea Level Rise and Benefits of Coastal Protection.”Fu and Song, “Assessing the Economic Costs of Sea Level Rise and Benefits of Coastal Protection.”

Fu, Xinyu and Jie Song. “Assessing the Economic Costs of Sea Level Rise and Benefits of Coastal Protection: A Spatiotemporal Approach” Sustainability 9, 1495 (2017).

Kunreuther, Howard. Limited Knowledge and Insurance Protection: Implications for Natural Hazard Policy. Springfield, Va.: National Technical Information Service, 1977. [https://catalog.hathitrust.org/Record/102012993](https://catalog.hathitrust.org/Record/102012993).

Kunreuther, Howard, and Paul Slovic. “Economics, Psychology, and Protective Behavior.” The American Economic Review 68, no. 2 (1978): 64–69.

Mendelsohn, Robert, “Economic Model of Flood Control Infrastructure.”

National Hurricane Center. “Sea, Lake, and Overland Surges from Hurricanes (SLOSH).” Government Resource. NOAA. Accessed December 17, 2018. [https://www.nhc.noaa.gov/surge/slosh.php](https://www.nhc.noaa.gov/surge/slosh.php).

NOAA. “Station Home Page - NOAA Tides & Currents.” Government Resource. Tides and Currents. Accessed December 17, 2018. [https://tidesandcurrents.noaa.gov/stationhome.html?id=8467150](https://tidesandcurrents.noaa.gov/stationhome.html?id=8467150).

O’Donnell , James. “Sea Level Rise in Connecticut.” Department of Marine Sciences a nd Connecticut Institute for Res ilience and Climate Adaptation, March 27, 2018. [https://circa.uconn.edu/wp-content/uploads/sites/1618/2017/10/SeaLevelRiseConnecticutFinalDraft-Posted-3_27_18.pdf](https://circa.uconn.edu/wp-content/uploads/sites/1618/2017/10/SeaLevelRiseConnecticutFinalDraft-Posted-3_27_18.pdf).
