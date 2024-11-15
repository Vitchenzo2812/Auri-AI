/* eslint-disable @typescript-eslint/no-explicit-any */
import * as S from './styles'

interface Props {
  as?: keyof JSX.IntrinsicElements
  size: number
  color?: string
  weight?: number
  fontFamily?: string
  lineHeight?: number
  children: any
}

const Text = ({ 
  as = 'span', 
  size, 
  weight = 400, 
  color = '#000', 
  fontFamily, 
  lineHeight,
  children 
}: Props) => {
  return (
    <S.Text
      as={as}
      size={size}
      weight={weight}
      fontFamily={fontFamily}
      lineHeight={lineHeight}
      color={color}
    >
      {children}
    </S.Text>
  )
}

export default Text