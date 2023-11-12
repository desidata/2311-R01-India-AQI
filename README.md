## Visualising AQI of Indian Sates and Cities

Air Quality Index (AQI) has long been the most thrown-around metric to get the basic idea about the quality of air in and around specific geographic locations.

Each year, in the weeks leading to the onset of winter throughout India, we get reports of worsened air-quality in various places all other the country. The reasons for such unfortunate occurrings being both man-made and environmental. And of all places, the national capital of _Delhi_ perhaps bears the worst brunt of it.

To make matters worst, one of our most awaited festivals, the one of lights and fireworks - _Diwali/Deepavali_ - happens to fall very closely around this time of suffering air-quality. While we cannot help but partake in this once-in-a-year festival with our sun-soaked firecrackers, we should, at the same time, keep an eye out toward the environmental side of it.

--- 
While talks of clean-energy, discussions about policies to mitigate the ailing air-quality in some of the most important locations in the country are under the way, we take the opportunity to try and visualise the varying AQI at different places within India.

We gathered the corresponding data from [National Air Quality Index - India](https://airquality.cpcb.gov.in/AQI_India_Iframe/) web-portal. We consolidated the data for some specific time-duration to try and visualise the changes in AQI at _state_ and _city_ level.

The datasets cotain data at a hierarchical structure of : 
> **State** -> **Cities/Twons winthin the state** -> **Statios recording the AQI within each city/town**

In order to represent AQI at the State-level, we have considered the _**median**_ AQI across all cities/towns within a state, for a paricular day-hour timestamp.

We have produced _racing bar charts_ in order to represent the _Median AQI_ variations across India.

---
#### Here's a demo:

![](./animations/india_aqi_states20231112_225829.gif)

![](./animations/india_aqi_cities20231112_230610.gif)
