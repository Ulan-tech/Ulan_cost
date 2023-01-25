# Ulan_cost
- This cost estimation is aimed to calculate the cost of a part printed by a Laser Powder Bed Fusion (L-PBF).
- There are mainly two cases in the build platform:
1) Many parts of an assembly from a particular customer
2) Multiple parts requested from multiple customers

The latter case would require us to issue a quotation for a 3D-printed product per part within the same build job.
In this regard, first, cost estimation equation was established involving the cost of material used per part ( $C_{mat}$ ), cost of build job ( $C_{build}$ ) and post-processing cost ( $C_{post}$ ). Finally we can find the total cost as follows.<br>
$$C_{total}=\dfrac{1}{1-F}(\sum_{p} C_{mat}^p + C_{build} + C_{post})$$ <br>
Second, a cost per part was found by using the volume ratio of the number of a particular part multiplied by its volume divided by the total number of parts multiplied by their volumes times the total cost. Here how a cost per part $C_{i}$  looks like: 
<br>
$$C_{i} = C_{total}\dfrac{n_{i}V_{i}}{\sum_{j=1}n_{j}V{_j}}$$



